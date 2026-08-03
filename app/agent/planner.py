from app.tools.registry import ToolRegistry


class AgentPlanner:
    """
    Decides which tools should be executed
    for a user request.

    For now the planner is rule-based.

    Later it will become LLM-powered.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    def plan(
        self,
        message: str,
    ):
        lower = message.lower()

        plan = []

        # ----------------------------
        # Project Scan
        # ----------------------------

        if (
            ("scan" in lower and "project" in lower)
            or ("analyze" in lower and "project" in lower)
            or ("codebase" in lower)
        ):
            tool = self.registry.get("project_scan")

            if tool:
                plan.append(
                    (
                        tool,
                        {
                            "path": ".",
                        },
                    )
                )

        # ----------------------------
        # Directory Tree
        # ----------------------------

        if (
            "tree" in lower
            or "directory tree" in lower
        ):
            tool = self.registry.get(
                "directory_tree"
            )

            if tool:
                plan.append(
                    (
                        tool,
                        {
                            "path": ".",
                        },
                    )
                )

        # ----------------------------
        # File List
        # ----------------------------

        if any(
            word in lower
            for word in (
                "list files",
                "show files",
                "project files",
                "folder",
                "directory",
            )
        ):
            tool = self.registry.get(
                "filesystem"
            )

            if tool:
                plan.append(
                    (
                        tool,
                        {
                            "path": ".",
                            "recursive": "false",
                        },
                    )
                )

        # ----------------------------
        # Read File
        # ----------------------------

        extensions = (
            ".py",
            ".md",
            ".txt",
            ".json",
            ".toml",
            ".yaml",
            ".yml",
        )

        for word in message.split():

            cleaned = word.strip("\"'(),")

            if (
                "." in cleaned
                or "/" in cleaned
                or "\\" in cleaned
            ):
                tool = self.registry.get(
                    "read_file"
                )

                if tool:
                    plan.append(
                        (
                            tool,
                            {
                                "path": cleaned,
                            },
                        )
                    )

                break

        return plan