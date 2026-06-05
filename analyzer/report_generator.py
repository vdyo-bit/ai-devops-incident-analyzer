from datetime import datetime


def build_report(
    incident,
    classification,
    validation,
    safety,
    ai_response
):

    report = f"""
==================================================
AI DEVOPS INCIDENT REPORT
==================================================

Timestamp:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Pod:
{incident.get("pod_name", "Unknown")}

Namespace:
{incident.get("namespace", "Unknown")}

Incident Type:
{classification.get("incident_type", "Unknown")}

Classifier Confidence:
{classification.get("confidence", "Unknown")}

Classification Reason:
{classification.get("reason", "Unknown")}

Validator Status:
{"PASS" if validation["valid"] else "FAIL"}

Guardrails Status:
{"PASS" if safety["safe"] else "FAIL"}

==================================================
AI ANALYSIS
==================================================

{ai_response}

==================================================
END OF REPORT
==================================================
"""

    return report
