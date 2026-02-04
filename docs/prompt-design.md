## Prompt Design for Safe AI-Assisted Operations
### Goal
Make AI useful in operations without allowing it to:
- Guess root causes
- Hallucinate missing data
- Overstep human judgment
This document defines a structured prompt design framework used for incident analysis and system troubleshooting.

### Why Prompt Structure Matters
Unstructured prompts often cause AI systems to:
- Assume missing context
- Provide generic or unsafe advice
- Overfit to common failure patterns
To avoid this, every operational prompt must follow a fixed structure that enforces evidence-based reasoning.

### Prompt Design Principles
1. Role clarity
- The AI is an assistant, not a decision-maker
2. Explicit constraints
- Prevent guessing and hallucination
3. Separation of signal vs noise
- Metrics and logs are summarized, not dumped
4. Evidence-first reasoning
- Conclusions must be traceable to provided data
5. Confidence calibration
- AI must express uncertainty when appropriate

### Standard Prompt Template
### ROLE  
You are an SRE reviewing an incident.

### CONSTRAINTS
- Do not guess or infer missing data
- If data is insufficient, explicitly state so
- Rank multiple possible causes by likelihood
- Base conclusions only on provided evidence
- Separate facts from assumptions

### SYSTEM CONTEXT
- OS: Ubuntu 22.04.5 LTS
- Kernel: 6.8.0-90-generic
- Environment: VM (KVM)
- CPU cores: 2
- Memory: 3.8 GB
- Disk type: HDD
- Workload type: Monitoring stack

### INCIDENT SUMMARY
An incident was observed where system behavior deviated from normal operation during a defined time window. 
The goal is to analyze provided metrics and logs without assumptions.

### OBSERVED METRICS (Summarized)
- CPU usage: Idle ~65%, no sustained CPU saturation
- Memory usage: Stable, no swapping observed
- Disk I/O: %util sustained near 95%, await increased significantly
- Network: No packet loss or saturation observed
- Error rates: Application error rate increased from baseline

### OBSERVED LOGS
- systemd: Service restart observed

### QUESTIONS
- What are the most likely root causes?
- What is your confidence level and why?
- What data is missing to confirm the root cause?
- What should be checked next, in priority order?

### OUTPUT FORMAT
- Bullet points only
- No speculation
- Clear reasoning per point

### Example Usage
- This prompt design is used for:
- Post-incident analysis (RCA)
- Performance bottleneck investigation
- Infrastructure anomaly triage
- AI-assisted learning without operational risk

### What This Prompt Explicitly Avoids
- Blind root-cause guessing
- One-size-fits-all troubleshooting
- Overconfident recommendations
- AI-driven production changes

### Human-in-the-Loop Guarantee
All AI-generated analysis:
- Must be reviewed by an engineer
- Is advisory only
- Does not trigger automated actions

### Summary
Structured prompt design transforms AI from:  
“Answer generator”  
into:  
“Evidence-driven reasoning assistant”  
This approach enables safe, reliable AI integration into DevOps and SRE workflows.
