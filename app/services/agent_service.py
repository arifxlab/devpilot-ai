from app.agent.engine import AgentEngine
from app.models.schemas import AgentRequest, AgentResponse


class AgentService:
    """
    Service layer responsible for coordinating requests
    between the API layer and the Agent Engine.
    """

    def __init__(self) -> None:
        self.engine = AgentEngine()

    async def process(self, request: AgentRequest) -> AgentResponse:
        """
        Process an agent request and return an API response.
        """

        result = await self.engine.run(request.message)

        return AgentResponse(
            answer=result.answer,
            success=True,
        )