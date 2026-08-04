from typing import Any


class ContextBuilder:
    """
    Builds structured context for the language model.

    Supports:
    - No tool execution
    - Single tool execution
    - Multiple tool execution

    This class is the single source responsible for converting
    raw tool outputs into LLM-ready context.
    """

    @staticmethod
    def build(
        user_request: str,
        tool_results: list[dict[str, Any]] | None = None,
    ) -> str:
        sections: list[str] = []

        sections.append("=" * 80)
        sections.append("USER REQUEST")
        sections.append("=" * 80)
        sections.append(user_request)
        sections.append("")

        sections.append("=" * 80)
        sections.append("TOOL RESULTS")
        sections.append("=" * 80)

        if not tool_results:
            sections.append("No tools were executed.")
        else:
            for index, item in enumerate(tool_results, start=1):
                tool_name = item.get("tool", "unknown")
                arguments = item.get("arguments", {})
                result = item.get("result", {})

                sections.append(f"[{index}] TOOL")
                sections.append(f"Name: {tool_name}")
                sections.append(f"Arguments: {arguments}")
                sections.append("Result:")
                sections.append(str(result))
                sections.append("-" * 80)

        sections.append("")
        sections.append("=" * 80)
        sections.append("INSTRUCTIONS")
        sections.append("=" * 80)
        sections.append(
            """
You are DevPilot AI, a software engineering assistant.

Rules:

1. Use ONLY the information contained in the tool results.

2. If multiple tools were executed, combine their findings into a
single coherent answer.

3. Never invent:
   - files
   - folders
   - code
   - project architecture
   - technologies

4. If information is missing,
say exactly what is missing.

5. Prefer concise technical explanations.

6. If a tool returned an error,
explain the error instead of guessing.

7. Answer like a senior backend engineer performing a code review.
""".strip()
        )

        return "\n".join(sections)