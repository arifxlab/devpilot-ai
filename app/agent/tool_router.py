from app.tools.registry import ToolRegistry


class ToolRouter:
    """
    Detects every tool required for a user request.

    Multiple tools may be executed for a
    single prompt.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    def detect(self, message: str):
        tools = self.detect_all(message)

        if tools:
            return tools[0]

        return None, None

    def detect_all(
        self,
        message: str,
    ):
        lower = message.lower()

        detected = []

        # -----------------------------
        # Project Scan
        # -----------------------------

        if (
            ("scan" in lower and "project" in lower)
            or ("analyze" in lower and "project" in lower)
            or ("scan" in lower and "codebase" in lower)
            or ("analyze" in lower and "codebase" in lower)
            or ("project overview" in lower)
            or ("project summary" in lower)
        ):
            detected.append(
                (
                    self.registry.get("project_scan"),
                    {
                        "path": ".",
                    },
                )
            )

        # -----------------------------
        # File List
        # -----------------------------

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
            detected.append(
                (
                    self.registry.get("filesystem"),
                    {
                        "path": ".",
                        "recursive": "false",
                    },
                )
            )

        # -----------------------------
        # Tree
        # -----------------------------

        if (
            "tree" in lower
            or "directory tree" in lower
            or "folder tree" in lower
        ):
            detected.append(
                (
                    self.registry.get("directory_tree"),
                    {
                        "path": ".",
                    },
                )
            )

        # -----------------------------
        # Read File
        # -----------------------------

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
            detected.append(
                (
                    self.registry.get("read_file"),
                    {
                        "path": self._extract_path(message),
                    },
                )
            )

        return [
            (tool, args)
            for tool, args in detected
            if tool is not None
        ]

    def _extract_path(
        self,
        message: str,
    ) -> str:
        for word in message.split():
            cleaned = word.strip("\"'(),")

            if (
                "." in cleaned
                or "/"
                in cleaned
                or "\\"
                in cleaned
            ):
                return cleaned

        return "README.md"