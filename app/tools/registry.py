from typing import Dict

from app.tools.base import BaseTool


class ToolRegistry:
    """
    Registry responsible for managing all available tools.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        """
        Register a new tool.
        """

        self._tools[tool.name] = tool

    def get(self, name: str) -> BaseTool | None:
        """
        Return a tool by name.
        """

        return self._tools.get(name)

    def all(self) -> list[BaseTool]:
        """
        Return all registered tools.
        """

        return list(self._tools.values())

    def count(self) -> int:
        """
        Return the number of registered tools.
        """

        return len(self._tools)