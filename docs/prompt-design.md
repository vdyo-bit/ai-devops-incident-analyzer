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
