import json
from pathlib import Path

from .prometheus_client import analyze_metrics
from .prompt_builder import build_report

def main():
    base_dir = Path(__file__).parent
    input_file = base_dir / "sample_input.json"

    with open(input_file, "r") as f:
        metrics = json.load(f)

    analysis = analyze_metrics(metrics)
    report = build_report(analysis)

    print(report)

if __name__ == "__main__":
    main()


