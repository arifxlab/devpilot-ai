from pathlib import Path
from typing import Any

from app.tools.base import BaseTool


class FileSystemTool(BaseTool):
    """
    Tool for inspecting directories.
    """

    @property
    def name(self) -> str:
        return "filesystem"

    @property
    def description(self) -> str:
        return "List files and directories."

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        path = Path(kwargs.get("path", "."))

        if not path.exists():
            return {
                "success": False,
                "error": f"Path does not exist: {path}",
            }

        if not path.is_dir():
            return {
                "success": False,
                "error": f"Not a directory: {path}",
            }

        directories: list[str] = []
        files: list[str] = []

        for item in sorted(path.iterdir()):
            if item.is_dir():
                directories.append(item.name)
            else:
                files.append(item.name)

        return {
            "success": True,
            "path": str(path.resolve()),
            "directories": directories,
            "files": files,
        }