from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """
    Request received by the AI agent.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="User message sent to the AI agent.",
    )

    session_id: str | None = Field(
        default=None,
        description="Existing conversation session identifier.",
    )


class AgentResponse(BaseModel):
    """
    Response returned by the AI agent.
    """

    answer: str = Field(
        ...,
        description="Generated response from the AI agent.",
    )

    success: bool = Field(
        default=True,
        description="Whether the request was processed successfully.",
    )

    session_id: str = Field(
        ...,
        description="Conversation session identifier.",
    )


class HealthResponse(BaseModel):
    """
    Health check response.
    """

    status: str
    application: str
    version: str