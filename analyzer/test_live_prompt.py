from k8s_collector import collect_pod_data
from k8s_parser import parse_pod_data
from ai_prompt_builder import build_prompt

data = collect_pod_data(
    "default",
    "oom-demo-7fc5d9f55-7dmx2"
)

incident = parse_pod_data(data)

prompt = build_prompt(incident)

print(prompt)
