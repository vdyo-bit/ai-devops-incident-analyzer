import os

from google import genai

from k8s_discovery import get_failing_pods
from k8s_collector import collect_pod_data
from k8s_parser import parse_pod_data
from k8s_incident_classifier import KubernetesIncidentClassifier

from ai_prompt_builder import build_prompt

from response_validator import validate_response
from ai_guardrails import check_guardrails

from report_generator import build_report


def main():

    namespace = "default"

    failing_pods = get_failing_pods(namespace)

    if not failing_pods:
        print("No failing pods detected.")
        return

    print("\nDetected failing pods:\n")

    for idx, pod in enumerate(
        failing_pods,
        start=1
    ):
        print(
            f"{idx}. {pod['pod_name']} ({pod['status']})"
        )

    pod_name = failing_pods[0]["pod_name"]

    print(
        f"\nAutomatically analyzing: {pod_name}\n"
    )

    print("[1/7] Collecting Kubernetes evidence...\n")

    pod_data = collect_pod_data(
        namespace,
        pod_name
    )

    print("[2/7] Parsing incident...\n")

    incident = parse_pod_data(
        pod_data
    )

    print("Parsed Incident:")
    print(incident)

    print("\n[3/7] Classifying incident...\n")

    classifier = KubernetesIncidentClassifier()

    classification = classifier.classify(
        incident
    )

    incident["classification"] = classification

    print("Classification:")
    print(classification)

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

    report_file = (
        f"reports/{incident['pod_name']}.txt"
    )

    with open(
        report_file,
        "w"
    ) as f:
        f.write(report)

    print("\n===== VALIDATION =====\n")
    print(validation)

    print("\n===== SAFETY =====\n")
    print(safety)

    print("\n===== INCIDENT REPORT =====\n")
    print(report)

    print(
        f"\nReport saved to: {report_file}"
    )


if __name__ == "__main__":
    main()
