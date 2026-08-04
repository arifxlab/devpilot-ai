from app.tools.registry import ToolRegistry


class AgentPlanner:
    """
    Responsible for deciding which tools should
    execute before the AI generates a response.

    This is currently a rule-based planner.

    Later it will be replaced with an LLM planner
    capable of reasoning about tool usage.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    def plan(self, message: str):
        """
        Build an execution plan consisting of one
        or more tools required to answer the request.
        """

        lower = message.lower()

        plan: list[tuple] = []
        used_tools: set[str] = set()

        def add_tool(name: str, arguments: dict):
            """
            Register a tool only once.
            """

            if name in used_tools:
                return

            tool = self.registry.get(name)

            if tool is None:
                return

            used_tools.add(name)
            plan.append((tool, arguments))

        # --------------------------------------------------
        # Project Scan
        # --------------------------------------------------

        if (
            ("scan" in lower and "project" in lower)
            or ("analyze" in lower and "project" in lower)
            or ("scan" in lower and "codebase" in lower)
            or ("analyze" in lower and "codebase" in lower)
            or ("project overview" in lower)
            or ("project summary" in lower)
            or ("inspect project" in lower)
        ):
            add_tool(
                "project_scan",
                {
                    "path": ".",
                },
            )

        # --------------------------------------------------
        # Directory Tree
        # --------------------------------------------------

        if (
            "tree" in lower
            or "directory tree" in lower
            or "folder tree" in lower
        ):
            add_tool(
                "directory_tree",
                {
                    "path": ".",
                },
            )

        # --------------------------------------------------
        # File Listing
        # --------------------------------------------------

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
            add_tool(
                "filesystem",
                {
                    "path": ".",
                    "recursive": "false",
                },
            )

        # --------------------------------------------------
        # Read File
        # --------------------------------------------------

        for word in message.split():
            cleaned = word.strip("\"'(),")

            if (
                "." in cleaned
                or "/" in cleaned
                or "\\" in cleaned
            ):
                add_tool(
                    "read_file",
                    {
                        "path": cleaned,
                    },
                )
                break

        # --------------------------------------------------
        # Default README
        # --------------------------------------------------

        if (
            "readme" in lower
            and "read_file" not in used_tools
        ):
            add_tool(
                "read_file",
                {
                    "path": "README.md",
                },
            )

        return plan