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
    Core AI agent responsible for orchestrating prompts,
    memory, tools, and the language model provider.
    """

    def __init__(self) -> None:
        self.provider = LocalProvider()
        self.memory = InMemoryStore()
        self.tool_registry = ToolRegistry()
        self.system_prompt = SYSTEM_PROMPT

    async def run(self, user_message: str) -> AgentResult:
        """
        Process a user request and return an agent result.
        """

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
            "Processing request with %d messages using provider '%s'.",
            len(conversation),
            self.provider.name,
        )

        answer = await self.provider.generate(
            system_prompt=self.system_prompt,
            user_prompt=user_message,
        )

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