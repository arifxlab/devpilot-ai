from pathlib import Path
from typing import Any

from app.tools.base import BaseTool


class FileSystemTool(BaseTool):
    """
    Lists files and folders from the local filesystem.
    """

    @property
    def name(self) -> str:
        return "filesystem"

    @property
    def description(self) -> str:
        return "Browse directories and inspect project files."

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        path = Path(kwargs.get("path", ".")).expanduser()

        recursive = str(kwargs.get("recursive", "false")).lower() == "true"
        max_items = int(kwargs.get("max_items", 200))

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

        items: list[dict[str, str]] = []

        iterator = path.rglob("*") if recursive else path.iterdir()

        for index, item in enumerate(iterator):
            if index >= max_items:
                break

            items.append(
                {
                    "name": item.name,
                    "path": str(item.resolve()),
                    "type": "directory" if item.is_dir() else "file",
                }
            )

        return {
            "success": True,
            "root": str(path.resolve()),
            "count": len(items),
            "items": items,
        }