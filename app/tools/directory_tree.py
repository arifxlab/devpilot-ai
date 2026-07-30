from pathlib import Path
from typing import Any

from app.tools.base import BaseTool


class DirectoryTreeTool(BaseTool):
    """
    Generate a readable directory tree.
    """

    MAX_DEPTH = 3

    @property
    def name(self) -> str:
        return "directory_tree"

    @property
    def description(self) -> str:
        return "Generate a directory tree."

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        root = Path(kwargs.get("path", "."))

        if not root.exists():
            return {
                "success": False,
                "error": f"Path does not exist: {root}",
            }

        if not root.is_dir():
            return {
                "success": False,
                "error": f"Not a directory: {root}",
            }

        tree: list[str] = []

        self._build_tree(
            root=root,
            lines=tree,
            prefix="",
            depth=0,
        )

        return {
            "success": True,
            "path": str(root.resolve()),
            "tree": "\n".join(tree),
        }

    def _build_tree(
        self,
        root: Path,
        lines: list[str],
        prefix: str,
        depth: int,
    ) -> None:
        if depth > self.MAX_DEPTH:
            return

        items = sorted(
            root.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower()),
        )

        for index, item in enumerate(items):
            connector = "└── " if index == len(items) - 1 else "├── "

            lines.append(f"{prefix}{connector}{item.name}")

            if item.is_dir():
                extension = "    " if index == len(items) - 1 else "│   "

                self._build_tree(
                    root=item,
                    lines=lines,
                    prefix=prefix + extension,
                    depth=depth + 1,
                )