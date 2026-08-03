from typing import Any


class ContextBuilder:
    """
    Builds structured context for the language model
    from either a single tool or multiple tool executions.
    """

    @staticmethod
    def build(
        user_request: str,
        tool_name: str,
        tool_result: Any,
    ) -> str:
        # ----------------------------------------
        # Multiple tool results
        # ----------------------------------------
        if isinstance(tool_result, list):
            sections: list[str] = []

            for item in tool_result:
                tool = item.get("tool", "unknown")
                result = item.get("result", item)

                sections.append(
                    f"""
==================================================
Tool: {tool}

Result:
{result}
==================================================
""".strip()
                )

            tools_output = "\n\n".join(sections)

            return f"""
You are an expert software engineering assistant.

The user asked:

{user_request}

The following information was collected from MULTIPLE project tools.

{tools_output}

Instructions:

- Use information from ALL tool results.
- Combine the information into one coherent explanation.
- Do not focus on only one tool.
- If multiple tools agree, combine their findings.
- If information is missing, clearly say so.
- Never invent project details.
- Answer like a senior software engineer reviewing the project.
"""

        # ----------------------------------------
        # Single tool result
        # ----------------------------------------
        return f"""
You are an expert software engineering assistant.

The user asked:

{user_request}

Tool Used:

{tool_name}

Tool Result:

{tool_result}

Instructions:

- Use ONLY this tool result.
- Explain it naturally.
- Do not invent information.
- If the tool failed, explain why.
- Answer clearly and professionally.
"""