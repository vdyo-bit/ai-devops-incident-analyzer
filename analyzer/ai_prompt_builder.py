def build_prompt(incident):

    logs = "\n".join(incident["logs"])

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
- Root Cause(s)
- Confidence
- Missing Data
- Next Investigation Steps

Do not provide remediation commands.
Do not speculate beyond available evidence.
"""
