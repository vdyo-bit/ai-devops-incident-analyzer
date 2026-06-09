import subprocess
import time


CHECK_INTERVAL = 300


def run_linux_analysis():

    print("\n===== LINUX CHECK =====\n")

    subprocess.run(
        [
            "python",
            "analyzer/live_linux_ai_analyzer.py"
        ]
    )


def run_k8s_analysis():

    print("\n===== KUBERNETES CHECK =====\n")

    subprocess.run(
        [
            "python",
            "analyzer/live_k8s_ai_analyzer.py"
        ]
    )


def main():

    print(
        "\nAI DevOps Monitoring Service Started\n"
    )

    print(
        f"Checking every {CHECK_INTERVAL} seconds\n"
    )

    while True:

        try:

            run_linux_analysis()

        except Exception as e:

            print(
                f"Linux monitoring error: {e}"
            )

        try:

            run_k8s_analysis()

        except Exception as e:

            print(
                f"Kubernetes monitoring error: {e}"
            )

        print(
            f"\nSleeping {CHECK_INTERVAL} seconds...\n"
        )

        time.sleep(
            CHECK_INTERVAL
        )


if __name__ == "__main__":
    main()
