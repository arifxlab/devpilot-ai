from dataclasses import dataclass, field

from app.providers.base import ChatMessage


@dataclass(slots=True)
class Conversation:
    """
    Represents a single conversation between the user
    and the AI agent.
    """

    messages: list[ChatMessage] = field(default_factory=list)

    def add_system(self, content: str) -> None:
        self.messages.append(
            ChatMessage(
                role="system",
                content=content,
            )
        )

    def add_user(self, content: str) -> None:
        self.messages.append(
            ChatMessage(
                role="user",
                content=content,
            )
        )

    def add_assistant(self, content: str) -> None:
        self.messages.append(
            ChatMessage(
                role="assistant",
                content=content,
            )
        )

    def history(self) -> list[ChatMessage]:
        """
        Return a copy of the conversation history.
        """
        return list(self.messages)

    def clear(self) -> None:
        """
        Remove all messages.
        """
        self.messages.clear()

    def size(self) -> int:
        """
        Number of messages in the conversation.
        """
        return len(self.messages)