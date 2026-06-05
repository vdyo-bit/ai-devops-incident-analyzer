import os

from google import genai

from k8s_collector import collect_pod_data
from k8s_parser import parse_pod_data
from k8s_incident_classifier import KubernetesIncidentClassifier

from ai_prompt_builder import build_prompt
from response_validator import validate_response
from ai_guardrails import check_guardrails


def main():

    namespace = "default"

    pod_name = input("Pod Name: ").strip()

    print("\nCollecting Kubernetes evidence...\n")

    pod_data = collect_pod_data(
        namespace,
        pod_name
    )

    incident = parse_pod_data(pod_data)

    classifier = KubernetesIncidentClassifier()

    classification = classifier.classify(
        incident
    )

    incident["classification"] = classification

    print("Classification:")
    print(classification)

    print("\nBuilding prompt...\n")

    prompt = build_prompt(incident)

    client = genai.Client(
        api_key=os.environ["GOOGLE_API_KEY"]
    )

    print("Sending to Gemini...\n")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_response = response.text

    print("Validating response...\n")

    validation = validate_response(
        ai_response
    )

    safety = check_guardrails(
        ai_response
    )

    print("\n===== VALIDATION =====\n")
    print(validation)

    print("\n===== SAFETY =====\n")
    print(safety)

    print("\n===== AI ANALYSIS =====\n")
    print(ai_response)


if __name__ == "__main__":
    main()
