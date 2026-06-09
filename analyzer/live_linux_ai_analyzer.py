import os

from google import genai
from datetime import datetime
from prometheus_client import analyze_metrics
from incident_classifier import IncidentClassifier

from ai_prompt_builder import build_prompt

from response_validator import validate_response
from ai_guardrails import check_guardrails

from report_generator import build_report


def main():

    print("\n[1/7] Loading metrics...\n")

    metrics = {
        "cpu_idle_pct": [2],
        "load_1m": [6],
        "memory_available_mb": [300],
        "disk_io_time": [0.15],
        "node_up": True,
        "cpu_cores": 2
    }

    print("[2/7] Analyzing metrics...\n")

    incident_data = analyze_metrics(
        metrics
    )

    print("Analysis:")
    print(incident_data)

    print("\n[3/7] Classifying incident...\n")

    classifier = IncidentClassifier()

    classification = classifier.classify(
        incident_data
    )

    print(classification)

    incident = {
        "incident_name":
            classification["incident_type"],

        "system_context": {
            "os": "Ubuntu 22.04",
            "cpu_cores": 2,
            "memory_gb": 4
        },

        "metrics": {
            "cpu_usage": "98%",
            "load_average": "6",
            "memory": "300 MB available",
            "swap": "unknown",
            "disk": "15% io wait"
        },

        "logs": [
            classification["reason"]
        ]
    }

    print("\n[4/7] Building prompt...\n")

    prompt = build_prompt(
        incident
    )

    print("[5/7] Sending to Gemini...\n")

    client = genai.Client(
        api_key=os.environ["GOOGLE_API_KEY"]
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_response = response.text

    print("[6/7] Validating response...\n")

    validation = validate_response(
        ai_response
    )

    safety = check_guardrails(
        ai_response
    )

    print("[7/7] Generating report...\n")

    report = build_report(
        incident,
        classification,
        validation,
        safety,
        ai_response
    )

    os.makedirs(
        "reports",
        exist_ok=True
    )

    from datetime import datetime

    timestamp = datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )

    report_file = (
        f"reports/linux-{timestamp}.txt"
    )

    with open(report_file, "w") as f:
        f.write(report)

    print(report)

    print(
        f"\nReport saved to: {report_file}"
    )


if __name__ == "__main__":
    main()
