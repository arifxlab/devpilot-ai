from typing import Any


class MultiContextBuilder:
    """
    Builds a single context block from multiple
    tool results.

    The LLM receives every tool output together
    so it can generate one coherent response.
    """

    @staticmethod
    def build(
        user_request: str,
        tool_results: list[dict[str, Any]],
    ) -> str:
        context = [
            f"User Request:\n{user_request}\n",
            "Tool Results:\n",
        ]

        for item in tool_results:
            context.append(
                f"""
----------------------------------------
Tool:
{item["tool"]}

Result:
{item["result"]}
"""
            )

        context.append(
            """
Instructions:

- Answer ONLY using the tool results.
- Combine information from every tool.
- If information is missing, say so.
- Never invent files, code or project details.
- Write naturally.
"""
        )

        return "\n".join(context)