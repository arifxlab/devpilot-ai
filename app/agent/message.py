from enum import Enum

from pydantic import BaseModel, Field


class Role(str, Enum):
    """
    Supported conversation roles.
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class AgentMessage(BaseModel):
    """
    Represents a single conversation message exchanged
    between the user, the assistant, or a tool.
    """

    role: Role = Field(
        ...,
        description="Role of the message sender.",
    )

    content: str = Field(
        ...,
        min_length=1,
        description="Message content.",
    )