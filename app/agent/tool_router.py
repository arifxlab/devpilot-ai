from app.tools.registry import ToolRegistry


class ToolRouter:
    """
    Routes natural language requests
    to the appropriate tool.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    def detect(self, message: str):
        lower = message.lower()

        # ----------------------------------
        # Project Scan Tool
        # ----------------------------------
        if (
            ("scan" in lower and "project" in lower)
            or ("analyze" in lower and "project" in lower)
            or ("scan" in lower and "codebase" in lower)
            or ("analyze" in lower and "codebase" in lower)
            or ("project overview" in lower)
            or ("project summary" in lower)
        ):
            return self.registry.get("project_scan"), {
                "path": ".",
            }

        # ----------------------------------
        # File Listing Tool
        # ----------------------------------
        if any(
            keyword in lower
            for keyword in (
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

        # ----------------------------------
        # Directory Tree Tool
        # ----------------------------------
        if (
            "tree" in lower
            or "directory tree" in lower
            or "folder tree" in lower
        ):
            return self.registry.get("directory_tree"), {
                "path": ".",
            }

        # ----------------------------------
        # Read File Tool
        # ----------------------------------
        if any(
            keyword in lower
            for keyword in (
                "read",
                "open",
                "show file",
                "display file",
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
            cleaned = word.strip("\"'(),")

            if (
                "." in cleaned
                or "/" in cleaned
                or "\\" in cleaned
            ):
                return cleaned

        return "README.md"