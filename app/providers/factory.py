from app.config.settings import settings
from app.providers.base import BaseProvider
from app.providers.ollama_provider import OllamaProvider


class ProviderFactory:
    """
    Factory responsible for creating LLM provider instances.
    """

    @staticmethod
    def create() -> BaseProvider:
        provider = settings.llm_provider.lower()

        if provider == "ollama":
            return OllamaProvider(
                host=settings.ollama_host,
                default_model=settings.ollama_model,
            )

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )