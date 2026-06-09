# analyzer/k8s_parser.py

import re


def parse_pod_data(pod_data):

    describe = pod_data["describe"]

    incident = {
        "source": "kubernetes",
        "pod_name": pod_data["pod_name"],
        "namespace": pod_data["namespace"]
    }

    # Current State Reason
    current_reason_match = re.search(
        r"State:\s+Waiting\s+Reason:\s+([A-Za-z0-9]+)",
        describe,
        re.MULTILINE
    )

    if current_reason_match:
        incident["current_reason"] = current_reason_match.group(1)

    # Last State Reason
    last_reason_match = re.search(
        r"Last State:\s+Terminated\s+Reason:\s+([A-Za-z0-9]+)",
        describe,
        re.MULTILINE
    )

    if last_reason_match:
        incident["last_reason"] = last_reason_match.group(1)

    # Exit Code
    exit_code_match = re.search(
        r"Exit Code:\s+(\d+)",
        describe
    )

    if exit_code_match:
        incident["exit_code"] = exit_code_match.group(1)

    # Restart Count
    restart_match = re.search(
        r"Restart Count:\s+(\d+)",
        describe
    )

    if restart_match:
        incident["restart_count"] = restart_match.group(1)

    # Container Name
    container_match = re.search(
        r"Containers:\s*\n\s*([A-Za-z0-9\-_]+):",
        describe
    )

    if container_match:
        incident["container_name"] = (
            container_match.group(1)
        )

    # Container Image
    image_match = re.search(
        r"Image:\s+(.+)",
        describe
    )

    if image_match:
        incident["image"] = (
            image_match.group(1).strip()
        )

    # Node Name
    node_match = re.search(
        r"Node:\s+([^\s/]+)",
        describe
    )

    if node_match:
        incident["node"] = (
            node_match.group(1)
        )

    # Memory Limit
    memory_limit_match = re.search(
        r"Limits:\s*\n\s*memory:\s*([^\n]+)",
        describe
    )

    if memory_limit_match:
        incident["memory_limit"] = (
            memory_limit_match.group(1).strip()
        )

    # Memory Request
    memory_request_match = re.search(
        r"Requests:\s*\n\s*memory:\s*([^\n]+)",
        describe
    )

    if memory_request_match:
        incident["memory_request"] = (
            memory_request_match.group(1).strip()
        )

    # Previous Container Logs
    incident["logs"] = pod_data["logs"]

    return incident
