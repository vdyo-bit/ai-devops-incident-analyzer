import os
import subprocess

from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


@app.route("/")
def home():

    reports_dir = "reports"

    reports = []

    if os.path.exists(reports_dir):
        reports = sorted(
            os.listdir(reports_dir),
            reverse=True
        )

    total_reports = len(reports)

    linux_reports = len(
        [r for r in reports if "linux" in r.lower()]
    )

    k8s_reports = total_reports - linux_reports

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

    return render_template(
        "report.html",
        filename=filename,
        content=content
    )


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
