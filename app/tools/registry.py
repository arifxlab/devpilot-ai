from typing import Dict

from app.tools.base import BaseTool
from app.tools.directory_tree import DirectoryTreeTool
from app.tools.filesystem import FileSystemTool
from app.tools.read_file import ReadFileTool
from app.tools.project_scan import ProjectScanTool
from app.tools.python_analyzer import PythonAnalyzerTool

class ToolRegistry:
    """
    Registry responsible for managing all available tools.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, BaseTool] = {}
        self._register_default_tools()

    def _register_default_tools(self) -> None:
        """
        Register all built-in tools.
        """

        self.register(FileSystemTool())
        self.register(ReadFileTool())
        self.register(DirectoryTreeTool())
        self.register(ProjectScanTool())
        self.register(PythonAnalyzerTool())

    def register(self, tool: BaseTool) -> None:
        """
        Register a tool.
        """

        self._tools[tool.name] = tool

    def get(self, name: str) -> BaseTool | None:
        """
        Return a tool by name.
        """

        return self._tools.get(name)

    def all(self) -> list[BaseTool]:
        """
        Return every registered tool.
        """

        return list(self._tools.values())

    def count(self) -> int:
        """
        Number of registered tools.
        """

        return len(self._tools)