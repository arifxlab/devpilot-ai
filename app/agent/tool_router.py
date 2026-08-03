from app.tools.registry import ToolRegistry


class ToolRouter:
    """
    Very small router that decides whether
    a request should execute a tool.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    def detect(self, message: str):
        lower = message.lower()

        if any(
            word in lower
            for word in (
                "list files",
                "show files",
                "project files",
                "directory",
                "folder",
            )
        ):
            return self.registry.get("filesystem"), {
                "path": ".",
                "recursive": "false",
            }

        if "tree" in lower:
            return self.registry.get("directory_tree"), {
                "path": ".",
            }

        if any(
            keyword in lower
            for keyword in (
                "read",
                "open",
                "show file",
                ".py",
                ".md",
                ".txt",
                ".json",
                ".toml",
                ".yaml",
                ".yml",
            )
        ):
            return self.registry.get("read_file"), {
                "path": self._extract_path(message),
            }

        return None, None

    def _extract_path(self, message: str) -> str:
        """
        Extract a likely file path from the prompt.
        """

        for word in message.split():
            cleaned = word.strip("\"'")

            if (
                "." in cleaned
                or "/" in cleaned
                or "\\" in cleaned
            ):
                return cleaned

        return "README.md"