from typing import Any

from app.agent.planner import AgentPlanner


class MultiToolExecutor:
    """
    Executes every tool selected by the planner.

    The planner determines which tools are required
    for a user's request, and the executor runs them
    in sequence.
    """

    def __init__(self) -> None:
        self.planner = AgentPlanner()

    async def execute(
        self,
        message: str,
    ) -> list[dict[str, Any]]:
        plan = self.planner.plan(message)

        results: list[dict[str, Any]] = []

        for tool, arguments in plan:
            result = await tool.execute(**arguments)

            results.append(
                {
                    "tool": tool.name,
                    "result": result,
                }
            )

        return results