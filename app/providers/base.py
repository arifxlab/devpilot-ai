from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """
    Represents a single message exchanged with an LLM.
    """

    role: str = Field(..., description="system, user or assistant")
    content: str = Field(..., description="Message content")


class ChatResponse(BaseModel):
    """
    Standard response returned by every provider.
    """

    content: str
    model: str
    provider: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    total_tokens: int | None = None


class BaseProvider(ABC):
    """
    Base interface for every LLM provider.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """
        Human-readable provider name.
        """

    @abstractmethod
    async def chat(
        self,
        messages: list[ChatMessage],
        model: str | None = None,
        temperature: float = 0.2,
    ) -> ChatResponse:
        """
        Generate a chat completion.
        """