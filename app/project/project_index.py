from app.project.models import ProjectScanResult
from app.project.scanner import ProjectScanner


class ProjectIndex:
    """
    Builds and caches a project scan.
    """

    def __init__(self) -> None:
        self.scanner = ProjectScanner()
        self._cache: ProjectScanResult | None = None

    def build(
        self,
        root: str = ".",
    ) -> ProjectScanResult:

        self._cache = self.scanner.scan(root)

        return self._cache

    @property
    def cache(self) -> ProjectScanResult | None:
        return self._cache