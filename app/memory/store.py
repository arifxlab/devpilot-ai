from app.memory.base import BaseMemory


class InMemoryStore(BaseMemory):
    """
    Simple in-memory key-value store used during development.
    """

    def __init__(self) -> None:
        self._storage: dict[str, str] = {}

    async def add(self, key: str, value: str) -> None:
        """
        Store a memory entry.
        """
        self._storage[key] = value

    async def get(self, key: str) -> str | None:
        """
        Retrieve a memory entry.
        """
        return self._storage.get(key)

    async def delete(self, key: str) -> None:
        """
        Delete a memory entry.
        """
        self._storage.pop(key, None)

    async def clear(self) -> None:
        """
        Remove all stored entries.
        """
        self._storage.clear()

    def size(self) -> int:
        """
        Return the number of stored entries.
        """
        return len(self._storage)