from dataclasses import dataclass, field
from uuid import uuid4

from app.memory.conversation import Conversation


@dataclass(slots=True)
class Session:
    """
    Represents an active conversation session.
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    conversation: Conversation = field(default_factory=Conversation)

    def reset(self) -> None:
        """
        Clear the current conversation while keeping
        the session identifier.
        """
        self.conversation.clear()

    @property
    def message_count(self) -> int:
        """
        Total number of messages in this session.
        """
        return self.conversation.size()