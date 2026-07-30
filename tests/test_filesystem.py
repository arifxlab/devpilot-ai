from pathlib import Path

import pytest

from app.tools.filesystem import FileSystemTool


@pytest.mark.anyio
async def test_filesystem_lists_directory(tmp_path: Path) -> None:
    """
    Verify the tool lists files and directories.
    """

    (tmp_path / "docs").mkdir()
    (tmp_path / "README.md").write_text("DevPilot AI")

    tool = FileSystemTool()

    result = await tool.execute(path=str(tmp_path))

    assert result["success"] is True
    assert "docs" in result["directories"]
    assert "README.md" in result["files"]


@pytest.mark.anyio
async def test_filesystem_invalid_path() -> None:
    """
    Verify an invalid path returns an error.
    """

    tool = FileSystemTool()

    result = await tool.execute(path="does_not_exist")

    assert result["success"] is False