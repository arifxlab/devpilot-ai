from typing import Any


class ContextBuilder:
    """
    Converts tool results into readable context that can
    be supplied to the language model.
    """

    @staticmethod
    def build(
        user_request: str,
        tool_name: str,
        tool_result: Any,
    ) -> str:
        return f"""
User Request:
{user_request}

Tool Used:
{tool_name}

Tool Result:
{tool_result}

Use ONLY the information above to answer the user's request.
Explain the result naturally.
Do not invent information.
"""