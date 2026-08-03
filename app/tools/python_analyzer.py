import ast
from pathlib import Path
from typing import Any

from app.tools.base import BaseTool


class PythonAnalyzerTool(BaseTool):
    """
    Analyze Python source code using the built-in AST module.
    """

    MAX_FILE_SIZE = 1024 * 1024  # 1 MB

    @property
    def name(self) -> str:
        return "python_analyzer"

    @property
    def description(self) -> str:
        return "Analyze a Python source file."

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        path = Path(kwargs.get("path", ""))

        if not path.exists():
            return {
                "success": False,
                "error": f"File does not exist: {path}",
            }

        if not path.is_file():
            return {
                "success": False,
                "error": f"Not a file: {path}",
            }

        if path.suffix != ".py":
            return {
                "success": False,
                "error": "Only Python files are supported.",
            }

        if path.stat().st_size > self.MAX_FILE_SIZE:
            return {
                "success": False,
                "error": "File exceeds the maximum supported size.",
            }

        try:
            source = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return {
                "success": False,
                "error": "Unable to decode file as UTF-8.",
            }

        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            return {
                "success": False,
                "error": f"Syntax error: {exc}",
            }

        imports: list[str] = []
        classes: list[str] = []
        functions: list[str] = []
        async_functions: list[str] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                imports.append(module)

            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)

            elif isinstance(node, ast.AsyncFunctionDef):
                async_functions.append(node.name)

        return {
            "success": True,
            "path": str(path.resolve()),
            "language": "Python",
            "lines": len(source.splitlines()),
            "characters": len(source),
            "imports": sorted(set(imports)),
            "classes": classes,
            "functions": functions,
            "async_functions": async_functions,
            "docstring": ast.get_docstring(tree),
        }