from time import perf_counter

from app.agent.message import AgentMessage, Role
from app.agent.provider import LocalProvider
from app.agent.response import AgentExecutionMetadata, AgentResult
from app.config.logging import get_logger
from app.memory.store import InMemoryStore
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.tools.registry import ToolRegistry

logger = get_logger(__name__)


class AgentEngine:
    """
    Core AI agent responsible for coordinating prompts,
    memory, tools, and the language model provider.
    """

    def __init__(self) -> None:
        self.provider = LocalProvider()
        self.memory = InMemoryStore()
        self.tool_registry = ToolRegistry()
        self.system_prompt = SYSTEM_PROMPT

    async def run(self, user_message: str) -> AgentResult:
        start_time = perf_counter()

        conversation = [
            AgentMessage(
                role=Role.SYSTEM,
                content=self.system_prompt,
            ),
            AgentMessage(
                role=Role.USER,
                content=user_message,
            ),
        ]

        logger.info(
            "Processing request using provider '%s'.",
            self.provider.name,
        )

        answer = await self._process_request(user_message)

        execution_time = perf_counter() - start_time

        metadata = AgentExecutionMetadata(
            model=self.provider.name,
            execution_time=execution_time,
            tool_calls=self.tool_registry.count(),
            memory_hits=0,
        )

        return AgentResult(
            answer=answer,
            metadata=metadata,
        )

    async def _process_request(self, message: str) -> str:
        """
        Route simple tool commands or fall back to the LLM provider.

        Temporary command format:

        tool:<tool_name> path=<path>
        """

        if message.startswith("tool:"):
            return await self._execute_tool_command(message)

        return await self.provider.generate(
            system_prompt=self.system_prompt,
            user_prompt=message,
        )

    async def _execute_tool_command(self, command: str) -> str:
        parts = command.split()

        tool_name = parts[0].replace("tool:", "")

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