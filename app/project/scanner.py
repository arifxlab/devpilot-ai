from pathlib import Path

from app.project.models import (
    ProjectFile,
    ProjectScanResult,
)


class ProjectScanner:
    """
    Scans a project directory and collects metadata.
    """

    EXCLUDED_DIRECTORIES = {
        ".git",
        ".idea",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        "node_modules",
    }

    def scan(
        self,
        root: str = ".",
    ) -> ProjectScanResult:

        project_root = Path(root).resolve()

        result = ProjectScanResult(
            root=str(project_root),
        )

        for item in project_root.rglob("*"):

            if any(
                excluded in item.parts
                for excluded in self.EXCLUDED_DIRECTORIES
            ):
                continue

            if item.is_dir():
                result.directories += 1
                continue

            result.total_files += 1

            if item.suffix == ".py":
                result.python_files += 1

            result.files.append(
                ProjectFile(
                    name=item.name,
                    path=str(item),
                    extension=item.suffix,
                    size=item.stat().st_size,
                )
            )

        return result