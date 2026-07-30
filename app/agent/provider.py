from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Abstract interface implemented by every LLM provider.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Name of the provider.
        """
        raise NotImplementedError

    @abstractmethod
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Generate a response from the language model.
        """
        raise NotImplementedError


class LocalProvider(LLMProvider):
    """
    Temporary placeholder provider.

    This implementation will later be replaced with
    OpenAI, Gemini, Ollama, Claude, or another provider.
    """

    @property
    def name(self) -> str:
        return "local-placeholder"

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return (
            "DevPilot AI is operational. "
            "LLM provider integration will be implemented in a future sprint."
        )