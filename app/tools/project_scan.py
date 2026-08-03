from typing import Any

from app.project.project_index import ProjectIndex
from app.tools.base import BaseTool


class ProjectScanTool(BaseTool):
    """
    Scan the current project and return metadata.
    """

    @property
    def name(self) -> str:
        return "project_scan"

    @property
    def description(self) -> str:
        return "Scan the current project."

    async def execute(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:

        root = kwargs.get("path", ".")

        index = ProjectIndex()

        result = index.build(root)

        return result.model_dump()