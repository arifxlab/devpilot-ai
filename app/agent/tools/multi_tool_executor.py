from typing import Any

from app.tools.registry import ToolRegistry


class MultiToolExecutor:
    """
    Executes multiple tools and combines their results
    into a single structured context.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    async def execute(
        self,
        tasks: list[tuple[str, dict[str, Any]]],
    ) -> list[dict[str, Any]]:
        """
        Execute tools sequentially.

        Args:
            tasks:
                [
                    ("project_scan", {"path": "."}),
                    ("directory_tree", {"path": "."}),
                    ("read_file", {"path": "README.md"}),
                ]

        Returns:
            List of tool execution results.
        """

        results: list[dict[str, Any]] = []

        for tool_name, arguments in tasks:
            tool = self.registry.get(tool_name)

            if tool is None:
                results.append(
                    {
                        "tool": tool_name,
                        "success": False,
                        "error": "Tool not registered.",
                    }
                )
                continue

            try:
                output = await tool.execute(**arguments)

                results.append(
                    {
                        "tool": tool_name,
                        "result": output,
                    }
                )

            except Exception as exc:
                results.append(
                    {
                        "tool": tool_name,
                        "success": False,
                        "error": str(exc),
                    }
                )

        return results