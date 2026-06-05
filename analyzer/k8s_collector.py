# analyzer/k8s_collector.py

import subprocess


def run_kubectl(command):

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stdout


def collect_pod_data(namespace, pod_name):

    describe_output = run_kubectl(
        ["kubectl", "describe", "pod", pod_name, "-n", namespace]
    )

    logs_output = run_kubectl(
        ["kubectl", "logs", pod_name, "-n", namespace, "--previous"]
    )

    return {
        "namespace": namespace,
        "pod_name": pod_name,
        "describe": describe_output,
        "logs": logs_output
    }


if __name__ == "__main__":

    data = collect_pod_data(
        "default",
        "oom-demo-7fc5d9f55-7dmx2"
    )

    print("\n===== POD DATA =====\n")

    print("Namespace:")
    print(data["namespace"])

    print("\nPod:")
    print(data["pod_name"])

    print("\n===== DESCRIBE =====\n")
    print(data["describe"])

    print("\n===== LOGS =====\n")
    print(data["logs"])
