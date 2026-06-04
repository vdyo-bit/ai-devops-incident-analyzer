"""
prompt_builder.py

Builds a structured, safety-constrained prompt for AI incident analysis.
The AI is instructed to critique evidence — not guess root causes.
"""

def build_prompt(
    system_context: dict,
    incident_summary: str,
    metrics_summary: str,
    log_snippets: str
) -> str:

    prompt = f"""
ROLE:
You are an SRE reviewing an incident.
Your task is to critique evidence, not guess.

CONSTRAINTS:
- Do not hallucinate or invent causes
- If data is insufficient, say so clearly
- Rank possible causes if ambiguity exists
- Separate facts from assumptions
- Base reasoning only on provided evidence

SYSTEM CONTEXT:
OS: {system_context.get("os", "Unknown")}
Kernel: {system_context.get("kernel", "Unknown")}
Environment: {system_context.get("environment", "Unknown")}
CPU cores: {system_context.get("cpu", "Unknown")}
Memory: {system_context.get("memory", "Unknown")}
Disk type: {system_context.get("disk", "Unknown")}
Workload type: {system_context.get("workload", "Unknown")}

INCIDENT SUMMARY:
{incident_summary}

OBSERVED METRICS (Summarized):
{metrics_summary}

OBSERVED LOGS (Relevant Only):
{log_snippets}

QUESTIONS:
1. Most likely root causes (ranked)
2. Confidence level with justification
3. What data is missing?
4. What should be checked next?

OUTPUT FORMAT:
- Bullet points
- Evidence-driven reasoning
- No speculation
"""

    return prompt


# Example usage (for testing)
if __name__ == "__main__":

    system_context = {
        "os": "Ubuntu 22.04.5",
        "kernel": "6.8.0-90-generic",
        "environment": "VM (KVM)",
        "cpu": "2",
        "memory": "3.8GB",
        "disk": "HDD",
        "workload": "Monitoring stack"
    }

    incident_summary = (
        "A controlled incident caused degraded system responsiveness "
        "during a test window."
    )

    metrics_summary = (
        "- CPU idle ~60%\n"
        "- Disk utilization near 95%\n"
        "- Elevated I/O wait"
    )

    log_snippets = (
        "kernel: blk_update_request: I/O delay observed\n"
        "prometheus: write latency increased"
    )

    prompt = build_prompt(
        system_context,
        incident_summary,
        metrics_summary,
        log_snippets
    )

    print(prompt)
