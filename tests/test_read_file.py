from pathlib import Path

import pytest

from app.tools.read_file import ReadFileTool


@pytest.mark.anyio
async def test_read_file_success(tmp_path: Path) -> None:
    """
    Verify reading a valid UTF-8 text file.
    """

    file = tmp_path / "example.txt"
    file.write_text(
        "Hello DevPilot AI\nSecond line",
        encoding="utf-8",
    )

    tool = ReadFileTool()

    result = await tool.execute(
        path=str(file)
    )

    assert result["success"] is True
    assert result["content"] == "Hello DevPilot AI\nSecond line"
    assert result["lines"] == 2


@pytest.mark.anyio
async def test_read_file_missing_file() -> None:
    """
    Verify missing files return an error.
    """

    tool = ReadFileTool()

    result = await tool.execute(
        path="missing_file.txt"
    )

    assert result["success"] is False


@pytest.mark.anyio
async def test_read_file_directory_error(tmp_path: Path) -> None:
    """
    Verify directories cannot be read as files.
    """

    tool = ReadFileTool()

    result = await tool.execute(
        path=str(tmp_path)
    )

    assert result["success"] is False