import os
import subprocess

from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


def extract_report_details(filename):

    incident_type = "Unknown"
    confidence = "Unknown"

    report_path = os.path.join(
        "reports",
        filename
    )

    try:

        with open(report_path, "r") as f:
            content = f.read()

        if "cpu_saturation" in content.lower():
            incident_type = "CPU Saturation"

        elif "memory_pressure" in content.lower():
            incident_type = "Memory Pressure"

        elif "oomkilled" in content.lower():
            incident_type = "OOMKilled"

        elif "crashloopbackoff" in content.lower():
            incident_type = "CrashLoopBackOff"

        elif "imagepullbackoff" in content.lower():
            incident_type = "ImagePullBackOff"

        if "Classifier Confidence:" in content:

            confidence = (
                content
                .split("Classifier Confidence:")[1]
                .split("\n")[1]
                .strip()
            )

    except Exception:
        pass

    return {
        "filename": filename,
        "incident_type": incident_type,
        "confidence": confidence,
        "category":
            "Linux"
            if "linux" in filename.lower()
            else "Kubernetes"
    }


@app.route("/")
def home():

    reports_dir = "reports"

    reports = []

    if os.path.exists(reports_dir):

        report_files = sorted(
            os.listdir(reports_dir),
            reverse=True
        )

        for report in report_files:

            reports.append(
                extract_report_details(
                    report
                )
            )

    total_reports = len(reports)

    linux_reports = len(
        [
            r for r in reports
            if r["category"] == "Linux"
        ]
    )

    k8s_reports = len(
        [
            r for r in reports
            if r["category"] == "Kubernetes"
        ]
    )

    return render_template(
        "index.html",
        reports=reports,
        total_reports=total_reports,
        linux_reports=linux_reports,
        k8s_reports=k8s_reports
    )


@app.route("/report/<filename>")
def report(filename):

    report_path = os.path.join(
        "reports",
        filename
    )

    if not os.path.exists(report_path):
        return "Report not found"

    with open(report_path, "r") as f:
        content = f.read()

    return f"""
    <html>
    <head>
        <title>{filename}</title>
        <style>
            body {{
                font-family: monospace;
                padding: 30px;
                background: #f5f5f5;
            }}

            pre {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                overflow-x: auto;
            }}

            a {{
                text-decoration: none;
            }}
        </style>
    </head>

    <body>

        <h2>{filename}</h2>

        <a href="/">← Back to Dashboard</a>

        <pre>{content}</pre>

    </body>
    </html>
    """


@app.route("/analyze-linux", methods=["POST"])
def analyze_linux():

    subprocess.Popen(
        [
            "python",
            "analyzer/live_linux_ai_analyzer.py"
        ]
    )

    return redirect("/")


@app.route("/analyze-k8s", methods=["POST"])
def analyze_k8s():

    subprocess.Popen(
        [
            "python",
            "analyzer/live_k8s_ai_analyzer.py"
        ]
    )

    return redirect("/")


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
