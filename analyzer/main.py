import json
from prometheus_client import analyze_metrics
from prompt_builder import build_report

def main():
    with open("sample_input.json", "r") as f:
        metrics = json.load(f)

    analysis = analyze_metrics(metrics)
    report = build_report(analysis)

    print(report)

if __name__ == "__main__":
    main()


