def validate_response(response: str):
    """
    Validate that the AI response contains
    all required analysis sections.
    """

    required_sections = [
        "Root Cause",
        "Confidence",
        "Missing Data"
    ]

    missing_sections = []

    for section in required_sections:
        if section not in response:
            missing_sections.append(section)

    return {
        "valid": len(missing_sections) == 0,
        "missing_sections": missing_sections
    }


if __name__ == "__main__":

    good_response = """
Root Cause:
CPU saturation

Confidence:
High

Missing Data:
Per-process CPU metrics
"""

    bad_response = """
CPU saturation detected.
"""

    print("GOOD RESPONSE TEST")
    print(validate_response(good_response))

    print("\nBAD RESPONSE TEST")
    print(validate_response(bad_response))
