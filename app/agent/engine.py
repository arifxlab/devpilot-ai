from time import perf_counter
from typing import Any

from app.agent.context_builder import ContextBuilder
from app.agent.response import AgentExecutionMetadata, AgentResult
from app.config.logging import get_logger
from app.memory.manager import MemoryManager
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.providers.base import ChatMessage
from app.providers.factory import ProviderFactory
from app.tools.multi_tool_executor import MultiToolExecutor

logger = get_logger(__name__)


class AgentEngine:
    """
    Core orchestration engine.

    Responsibilities:
        1. Manage conversation memory
        2. Execute tools
        3. Build LLM context
        4. Call the language model
        5. Return structured metadata
    """

    def __init__(self) -> None:
        self.provider = ProviderFactory.create()
        self.memory = MemoryManager()
        self.executor = MultiToolExecutor()
        self.system_prompt = SYSTEM_PROMPT

    async def run(
        self,
        user_message: str,
        session_id: str | None = None,
    ) -> AgentResult:
        """
        Main entrypoint for every request.
        """

        start = perf_counter()

        logger.info(
            "Processing request using provider '%s'.",
            self.provider.provider_name,
        )

        session = self.memory.get_or_create(session_id)

        if session.message_count == 0:
            session.conversation.add_system(
                self.system_prompt,
            )

        answer, tool_calls = await self._process_request(
            session=session,
            message=user_message,
        )

        elapsed = perf_counter() - start

        metadata = AgentExecutionMetadata(
            model=self.provider.provider_name,
            execution_time=elapsed,
            tool_calls=tool_calls,
            memory_hits=session.message_count,
            session_id=session.id,
        )

        return AgentResult(
            answer=answer,
            metadata=metadata,
        )

    async def _process_request(
        self,
        session: Any,
        message: str,
    ) -> tuple[str, int]:
        """
        Executes any required tools before sending
        the prompt to the language model.
        """

        tool_results = await self.executor.execute(message)

        session.conversation.add_user(message)

        # -----------------------------
        # Tool-assisted response
        # -----------------------------
        if tool_results:

            context = ContextBuilder.build(
                user_request=message,
                tool_results=tool_results,
            )

            history = list(session.conversation.history())

            history.append(
                ChatMessage(
                    role="user",
                    content=context,
                )
            )

            response = await self.provider.chat(history)

        # -----------------------------
        # Normal conversation
        # -----------------------------
        else:

            response = await self.provider.chat(
                session.conversation.history()
            )

        session.conversation.add_assistant(
            response.content,
        )

        logger.info(
            "Completed request (%d tool(s) executed).",
            len(tool_results),
        )

        return response.content, len(tool_results)