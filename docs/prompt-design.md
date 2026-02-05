# Prompt Engineering Iteration Log

## Prompt Goals

The primary goal was to make AI critique incident evidence instead of guessing root causes.  
The prompt was designed to enforce structured reasoning, uncertainty acknowledgment, and evidence-based analysis.

---

## Prompt Structure

Explicit sections were used to:

- Separate system context from observations
- Prevent raw metric dumping
- Force evidence-driven reasoning
- Reduce hallucination risk
- Maintain consistent AI behavior

This structure mirrors real SRE incident reviews.

---

## What Worked Well

- Explicit constraints prevented speculative root causes
- Summarized metrics improved signal clarity
- Structured questions guided AI reasoning
- Confidence reporting reduced overconfident responses

The AI consistently admitted when data was insufficient.

---

## Failure Modes Observed

- AI occasionally leaned toward common failure patterns
- Ambiguous metrics triggered overinterpretation
- Missing context sometimes led to ranked guesses

These behaviors reinforced the need for strict constraint wording.

---

## Prompt Adjustments

Adjustments included:

- Strengthening “do not guess” constraints
- Requiring explicit uncertainty statements
- Emphasizing evidence-only reasoning
- Clarifying output format expectations

These changes improved consistency and reduced hallucinated conclusions.

---

## Summary

Prompt engineering is treated as an iterative process.  
Structured constraints and clear context dramatically improve AI reliability for incident analysis.

The prompt now functions as a safety boundary, ensuring AI remains an advisory reasoning assistant.
