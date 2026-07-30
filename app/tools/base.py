from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Abstract base class for all DevPilot AI tools.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique tool name.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Short description of the tool.
        """
        raise NotImplementedError

    @abstractmethod
    async def execute(self, **kwargs: Any) -> Any:
        """
        Execute the tool.
        """
        raise NotImplementedError