from k8s_collector import collect_pod_data
from k8s_parser import parse_pod_data

data = collect_pod_data(
    "default",
    "oom-demo-7fc5d9f55-7dmx2"
)

incident = parse_pod_data(data)

print("\n===== PARSED INCIDENT =====\n")

for key, value in incident.items():
    print(f"{key}: {value}")
