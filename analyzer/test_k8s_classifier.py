from k8s_collector import collect_pod_data
from k8s_parser import parse_pod_data
from k8s_incident_classifier import KubernetesIncidentClassifier

data = collect_pod_data(
    "default",
    "oom-demo-7fc5d9f55-7dmx2"
)

incident = parse_pod_data(data)

classifier = KubernetesIncidentClassifier()

result = classifier.classify(incident)

print("\n===== INCIDENT =====\n")
print(incident)

print("\n===== CLASSIFICATION =====\n")
print(result)
