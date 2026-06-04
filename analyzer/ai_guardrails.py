def check_guardrails(response: str):
    """
    Detect unsafe actions and overconfident conclusions
    in AI-generated incident analysis.
    """

    blocked_phrases = [
        "run this command",
        "execute",
        "delete",
        "shutdown",
        "reboot",
        "restart production",
        "kill -9"
    ]

    certainty_phrases = [
        "definitely",
        "certainly",
        "guaranteed",
        "without doubt",
        "100%"
    ]

    violations = []

    response_lower = response.lower()

    # Detect unsafe actions
    for phrase in blocked_phrases:
        if phrase in response_lower:
            violations.append(
                f"Unsafe action detected: '{phrase}'"
            )

    # Detect overconfidence
    for phrase in certainty_phrases:
        if phrase in response_lower:
            violations.append(
                f"Overconfidence detected: '{phrase}'"
            )

    return {
        "safe": len(violations) == 0,
        "violations": violations
    }


if __name__ == "__main__":

    safe_response = """
Root Cause:
CPU saturation is a likely explanation.

Confidence:
Medium

Missing Data:
Per-process CPU metrics
"""

    unsafe_response = """
Root Cause:
CPU saturation

Run this command:
kill -9 1234

Confidence:
High

Missing Data:
Per-process metrics
"""

    overconfident_response = """
Root Cause:
This is definitely CPU saturation.

Confidence:
High

Missing Data:
None
"""

    print("SAFE RESPONSE TEST")
    print(check_guardrails(safe_response))

    print("\nUNSAFE RESPONSE TEST")
    print(check_guardrails(unsafe_response))

    print("\nOVERCONFIDENT RESPONSE TEST")
    print(check_guardrails(overconfident_response))
