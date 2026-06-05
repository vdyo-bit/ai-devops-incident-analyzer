import json
from pathlib import Path

from .prometheus_client import analyze_metrics
from .incident_classifier import IncidentClassifier


def main():

    base_dir = Path(__file__).parent
    input_file = base_dir / "sample_input.json"

    with open(input_file, "r") as f:
        metrics = json.load(f)

    # Step 1: Analyze metrics
    analysis = analyze_metrics(metrics)

    # Step 2: Classify incident
    classifier = IncidentClassifier()
    classification = classifier.classify(analysis)

    print("\n=== Metric Analysis ===")
    print(analysis)

    print("\n=== Incident Classification ===")
    print(classification)


if __name__ == "__main__":
    main()
