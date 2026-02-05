def build_prompt():

    return """
ROLE:
You are an SRE reviewing an incident.

CONSTRAINTS:
- Do not guess root causes
- Use only provided evidence
- Admit when data is insufficient
- Rank possible causes if needed

SYSTEM CONTEXT:
Ubuntu VM, 2 CPU cores, 4GB RAM

INCIDENT SUMMARY:
Controlled test incident caused degraded responsiveness.

OBSERVED METRICS:
- CPU idle ~65%
- Disk utilization near 95%
- Elevated I/O wait

OBSERVED LOGS:
systemd: service restart observed

QUESTIONS:
1. Most likely root causes
2. Confidence level
3. Missing data
4. What to check next

OUTPUT FORMAT:
- Bullet points
- Evidence-driven reasoning
- No speculation
"""
