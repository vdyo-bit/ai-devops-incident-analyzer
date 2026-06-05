# analyzer/k8s_parser.py

import re


def parse_pod_data(pod_data):

    describe = pod_data["describe"]

    incident = {
        "source": "kubernetes",
        "pod_name": pod_data["pod_name"],
        "namespace": pod_data["namespace"]
    }

    current_reason_match = re.search(
        r"State:\s+Waiting\s+Reason:\s+([A-Za-z0-9]+)",
        describe,
        re.MULTILINE
    )

    if current_reason_match:
        incident["current_reason"] = current_reason_match.group(1)

    last_reason_match = re.search(
        r"Last State:\s+Terminated\s+Reason:\s+([A-Za-z0-9]+)",
        describe,
        re.MULTILINE
    )

    if last_reason_match:
        incident["last_reason"] = last_reason_match.group(1)

    exit_code_match = re.search(
        r"Exit Code:\s+(\d+)",
        describe
    )

    if exit_code_match:
        incident["exit_code"] = exit_code_match.group(1)

    restart_match = re.search(
        r"Restart Count:\s+(\d+)",
        describe
    )

    if restart_match:
        incident["restart_count"] = restart_match.group(1)

    incident["logs"] = pod_data["logs"]

    return incident
