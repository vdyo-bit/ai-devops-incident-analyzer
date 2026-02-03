# main.py
from analyzer import prometheus_client
from analyzer import prompt_builder
import json

def main():
    with open("sample_input.json") as f:
        metrics = json.load(f)

    analysis = prometheus_client.analyze(metrics)

    report = prompt_builder.build_report(analysis)

    print(report)

if __name__ == "__main__":
    main()
