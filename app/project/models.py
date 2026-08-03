from pathlib import Path

from pydantic import BaseModel, Field


class ProjectFile(BaseModel):
    """
    Represents a discovered project file.
    """

    name: str
    path: str
    extension: str
    size: int


class ProjectScanResult(BaseModel):
    """
    Result produced after scanning a project.
    """

    root: str = Field(...)
    total_files: int = Field(default=0)
    python_files: int = Field(default=0)
    directories: int = Field(default=0)

    files: list[ProjectFile] = Field(
        default_factory=list,
    )