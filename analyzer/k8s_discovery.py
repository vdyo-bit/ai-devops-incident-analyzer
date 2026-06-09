import subprocess


def get_failing_pods(namespace="default"):

    result = subprocess.run(
        [
            "kubectl",
            "get",
            "pods",
            "-n",
            namespace,
            "--no-headers"
        ],
        capture_output=True,
        text=True
    )

    pods = []

    for line in result.stdout.splitlines():

        parts = line.split()

        if len(parts) < 3:
            continue

        pod_name = parts[0]
        status = parts[2]

        failing_statuses = [
            "CrashLoopBackOff",
            "ImagePullBackOff",
            "ErrImagePull",
            "OOMKilled",
            "Pending"
        ]

        if status in failing_statuses:

            pods.append({
                "pod_name": pod_name,
                "status": status
            })

    return pods


if __name__ == "__main__":

    failing = get_failing_pods()

    print("\nDetected failing pods:\n")

    for idx, pod in enumerate(failing, start=1):

        print(
            f"{idx}. {pod['pod_name']} ({pod['status']})"
        )
