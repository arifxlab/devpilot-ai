from pathlib import Path
from typing import Any

from app.tools.base import BaseTool


class ReadFileTool(BaseTool):
    """
    Safely read UTF-8 text files.
    """

    MAX_FILE_SIZE = 1024 * 1024  # 1 MB

    @property
    def name(self) -> str:
        return "read_file"

    @property
    def description(self) -> str:
        return "Read the contents of a UTF-8 text file."

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        path = Path(kwargs.get("path", ""))

        if not path.exists():
            return {
                "success": False,
                "error": f"File does not exist: {path}",
            }

        if not path.is_file():
            return {
                "success": False,
                "error": f"Not a file: {path}",
            }

        if path.stat().st_size > self.MAX_FILE_SIZE:
            return {
                "success": False,
                "error": "File exceeds the maximum supported size (1 MB).",
            }

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return {
                "success": False,
                "error": "File is not UTF-8 encoded.",
            }

        return {
            "success": True,
            "path": str(path.resolve()),
            "content": content,
            "lines": len(content.splitlines()),
            "characters": len(content),
        }