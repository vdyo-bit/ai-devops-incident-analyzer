def build_prompt(incident):

    logs = "\n".join(incident.get("logs", []))

    # -----------------------------
    # Linux Incident
    # -----------------------------
    if "system_context" in incident:

        return f"""
ROLE:
You are an SRE reviewing an incident.

CONSTRAINTS:
- Do not guess root causes
- Use only provided evidence
- Admit when data is insufficient
- Rank possible causes if needed

SYSTEM CONTEXT:
OS: {incident['system_context']['os']}
CPU Cores: {incident['system_context']['cpu_cores']}
Memory: {incident['system_context']['memory_gb']} GB

INCIDENT:
{incident['incident_name']}

OBSERVED METRICS:
CPU Usage: {incident['metrics'].get('cpu_usage', 'N/A')}
Load Average: {incident['metrics'].get('load_average', 'N/A')}
Memory: {incident['metrics'].get('memory', incident['metrics'].get('memory_available', 'N/A'))}
Swap: {incident['metrics'].get('swap', incident['metrics'].get('swap_usage', 'N/A'))}
Disk: {incident['metrics'].get('disk', incident['metrics'].get('disk_iowait', 'N/A'))}

OBSERVED LOGS:
{logs}

QUESTIONS:
1. What are the most likely root causes?
2. What is your confidence level (Low / Medium / High)?
3. What data is missing?
4. What should an engineer investigate next?

OUTPUT FORMAT:

Root Cause:
...

Confidence:
...

Missing Data:
...

Next Investigation:
...
"""

    # -----------------------------
    # Kubernetes Incident
    # -----------------------------
    elif "kubernetes_context" in incident:

        events = "\n".join(incident.get("events", []))

        return f"""
ROLE:
You are an SRE reviewing a Kubernetes incident.

CONSTRAINTS:
- Do not guess root causes
- Use only provided evidence
- Admit when data is insufficient
- Separate facts from assumptions

INCIDENT:
{incident['incident_name']}

KUBERNETES CONTEXT:

Cluster:
{incident['kubernetes_context'].get('cluster', 'N/A')}

Namespace:
{incident['kubernetes_context'].get('namespace', 'N/A')}

Deployment:
{incident['kubernetes_context'].get('deployment', 'N/A')}

Pod:
{incident['kubernetes_context'].get('pod', 'N/A')}

Status:
{incident['kubernetes_context'].get('status', 'N/A')}

Node:
{incident['kubernetes_context'].get('node', 'N/A')}

OBSERVED EVENTS:
{events}

OBSERVED LOGS:
{logs}

QUESTIONS:
1. What is the most likely root cause?
2. What evidence supports this conclusion?
3. What confidence level should be assigned?
4. What additional investigation is recommended?

OUTPUT FORMAT:

Root Cause:
...

Confidence:
...

Evidence:
...

Missing Data:
...

Next Investigation:
...
"""

    # -----------------------------
    # Unknown Incident Type
    # -----------------------------
    else:

        return f"""
ROLE:
You are an SRE.

The incident format is unknown.

Incident Data:
{incident}

Please identify:
- Possible root causes
- Missing information
- Recommended next steps
"""
