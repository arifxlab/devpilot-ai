from __future__ import annotations

from ollama import AsyncClient

from app.providers.base import BaseProvider, ChatMessage, ChatResponse


class OllamaProvider(BaseProvider):
    """
    Ollama LLM provider implementation.
    """

    def __init__(
        self,
        host: str = "http://localhost:11434",
        default_model: str = "llama3:latest",
    ) -> None:
        self._client = AsyncClient(host=host)
        self._default_model = default_model

    @property
    def provider_name(self) -> str:
        return "ollama"

    async def chat(
        self,
        messages: list[ChatMessage],
        model: str | None = None,
        temperature: float = 0.2,
    ) -> ChatResponse:
        """
        Generate a chat completion using Ollama.
        """

        selected_model = model or self._default_model

        response = await self._client.chat(
            model=selected_model,
            messages=[
                {
                    "role": message.role,
                    "content": message.content,
                }
                for message in messages
            ],
            options={
                "temperature": temperature,
            },
        )

        return ChatResponse(
            content=response.message.content,
            model=selected_model,
            provider=self.provider_name,
            prompt_tokens=None,
            completion_tokens=None,
            total_tokens=None,
        )