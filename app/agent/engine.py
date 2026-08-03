from time import perf_counter

from app.agent.context_builder import ContextBuilder
from app.agent.response import AgentExecutionMetadata, AgentResult
from app.agent.tool_router import ToolRouter
from app.config.logging import get_logger
from app.memory.manager import MemoryManager
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.providers.base import ChatMessage
from app.providers.factory import ProviderFactory
from app.tools.registry import ToolRegistry
from app.agent.tools.multi_tool_executor import MultiToolExecutor
from app.agent.multi_context_builder import MultiContextBuilder
from app.tools.multi_tool_executor import MultiToolExecutor
from app.providers.base import ChatMessage

logger = get_logger(__name__)


class AgentEngine:
    """
    Core AI agent responsible for coordinating prompts,
    memory, tools, and the language model provider.
    """

    def __init__(self) -> None:
        self.provider = ProviderFactory.create()
        self.memory = MemoryManager()
        self.tool_registry = ToolRegistry()
        self.tool_executor = MultiToolExecutor()
        self.system_prompt = SYSTEM_PROMPT
        self.multi_tool_executor = MultiToolExecutor()

    async def run(
        self,
        user_message: str,
        session_id: str | None = None,
    ) -> AgentResult:
        start_time = perf_counter()

        logger.info(
            "Processing request using provider '%s'.",
            self.provider.provider_name,
        )

        session = self.memory.get_or_create(session_id)

        if session.message_count == 0:
            session.conversation.add_system(
                self.system_prompt,
            )

        answer = await self._process_request(
            session=session,
            message=user_message,
        )

        execution_time = perf_counter() - start_time

        metadata = AgentExecutionMetadata(
            model=self.provider.provider_name,
            execution_time=execution_time,
            tool_calls=self.tool_registry.count(),
            memory_hits=session.message_count,
            session_id=session.id,
        )

        return AgentResult(
            answer=answer,
            metadata=metadata,
        )

    async def _process_request(
        self,
        session,
        message: str,
    ) -> str:
        """
        Process a request using either one tool,
        multiple tools, or the LLM.
        """

        lower = message.lower()

        # ----------------------------------------
        # Multi-tool project understanding
        # ----------------------------------------

        if any(
            phrase in lower
            for phrase in (
                "project architecture",
                "project structure",
                "backend architecture",
                "summarize project",
                "explain this project",
                "how is this project organized",
                "project overview",
            )
        ):
            tool_results = await self.multi_tool_executor.execute(
                [
                    ("project_scan", {"path": "."}),
                    ("directory_tree", {"path": "."}),
                    ("read_file", {"path": "README.md"}),
                ]
            )

            context = ContextBuilder.build(
                user_request=message,
                tool_name="multi_tool",
                tool_result=tool_results,
            )

            session.conversation.add_user(message)

            response = await self.provider.chat(
                session.conversation.history()
                + [
                    ChatMessage(
                        role="user",
                        content=context,
                    )
                ]
            )

            session.conversation.add_assistant(response.content)

            return response.content

        # ----------------------------------------
        # Single Tool
        # ----------------------------------------

        tool_results = await self.tool_executor.execute(message)

        if tool_results:
            context = MultiContextBuilder.build(
                user_request=message,
                tool_results=tool_results,
            )

            session.conversation.add_user(message)

            response = await self.provider.chat(
                session.conversation.history()
                + [
                    ChatMessage(
                        role="user",
                        content=context,
                    )
                ]
            )

            session.conversation.add_assistant(response.content)

            return response.content

        # ----------------------------------------
        # Normal Chat
        # ----------------------------------------

        session.conversation.add_user(message)

        response = await self.provider.chat(session.conversation.history())

        session.conversation.add_assistant(response.content)

        return response.content

    async def _execute_tool_command(
        self,
        command: str,
    ) -> str:
        """
        Execute a tool directly using the legacy
        tool:<name> syntax.
        """

        parts = command.split()

        tool_name = parts[0].replace(
            "tool:",
            "",
        )

        arguments: dict[str, str] = {}

        for token in parts[1:]:
            if "=" in token:
                key, value = token.split("=", 1)
                arguments[key] = value

        tool = self.tool_registry.get(tool_name)

        if tool is None:
            return f"Tool '{tool_name}' is not registered."

        result = await tool.execute(**arguments)

        return str(result)