from time import perf_counter

from app.agent.message import AgentMessage, Role
from app.agent.response import AgentExecutionMetadata, AgentResult
from app.config.logging import get_logger

logger = get_logger(__name__)


class AgentEngine:
    """
    Core AI agent responsible for coordinating conversations,
    retrieval, tools, and LLM interaction.
    """

    def __init__(self) -> None:
        self.system_prompt = (
            "You are DevPilot AI, a professional software engineering assistant. "
            "Provide accurate, concise, and practical engineering guidance. "
            "Do not invent project information."
        )

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
            "Processing request with %d conversation messages.",
            len(conversation),
        )

        # Placeholder until an LLM provider is integrated.
        answer = (
            "DevPilot AI is initialized successfully. "
            "LLM integration will be added in a later sprint."
        )

        execution_time = perf_counter() - start_time

        metadata = AgentExecutionMetadata(
            model="local-placeholder",
            execution_time=execution_time,
            tool_calls=0,
            memory_hits=0,
        )

        return AgentResult(
            answer=answer,
            metadata=metadata,
        )