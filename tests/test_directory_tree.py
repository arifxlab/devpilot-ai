from pathlib import Path

import pytest

from app.tools.directory_tree import DirectoryTreeTool


@pytest.mark.anyio
async def test_directory_tree_generates_structure(tmp_path: Path) -> None:
    """
    Verify directory tree generation.
    """

    src = tmp_path / "src"
    src.mkdir()

    file = src / "main.py"
    file.write_text(
        "print('hello')",
        encoding="utf-8",
    )

    tool = DirectoryTreeTool()

    result = await tool.execute(
        path=str(tmp_path)
    )

    assert result["success"] is True
    assert "src" in result["tree"]
    assert "main.py" in result["tree"]


@pytest.mark.anyio
async def test_directory_tree_invalid_path() -> None:
    """
    Verify invalid paths return an error.
    """

    tool = DirectoryTreeTool()

    result = await tool.execute(
        path="missing_directory"
    )

    assert result["success"] is False