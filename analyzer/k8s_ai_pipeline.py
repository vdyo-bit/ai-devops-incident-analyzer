from openai import OpenAI

from k8s_collector import collect_pod_data
from k8s_parser import parse_pod_data
from k8s_incident_classifier import KubernetesIncidentClassifier
from ai_prompt_builder import build_prompt
from response_validator import validate_response
from ai_guardrails import check_guardrails


def main():

    client = OpenAI()

    print("\nCollecting Kubernetes incident...\n")

    pod_data = collect_pod_data(
        "default",
        "oom-demo-7fc5d9f55-7dmx2"
    )

    incident = parse_pod_data(pod_data)

    classifier = KubernetesIncidentClassifier()

    classification = classifier.classify(incident)

    print("=== INCIDENT ===\n")
    print(incident)

    print("\n=== CLASSIFICATION ===\n")
    print(classification)

    prompt = build_prompt(incident)

    print("\n=== SENDING TO AI ===\n")

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    ai_response = response.output_text

    print("\n=== AI RESPONSE ===\n")
    print(ai_response)

    validation = validate_response(ai_response)

    print("\n=== VALIDATION ===\n")
    print(validation)

    guardrail_result = check_guardrails(ai_response)

    print("\n=== GUARDRAILS ===\n")
    print(guardrail_result)


if __name__ == "__main__":
    main()
