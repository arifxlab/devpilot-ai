from abc import ABC, abstractmethod


class BaseMemory(ABC):
    """
    Abstract base class for memory implementations.
    """

    @abstractmethod
    async def add(self, key: str, value: str) -> None:
        """
        Store a memory entry.
        """
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str) -> str | None:
        """
        Retrieve a memory entry by key.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, key: str) -> None:
        """
        Delete a memory entry.
        """
        raise NotImplementedError

    @abstractmethod
    async def clear(self) -> None:
        """
        Remove all memory entries.
        """
        raise NotImplementedError