# AI Behavior Evaluation — Incident Analysis

## Purpose

This document captures observations about how the AI behaves when analyzing incident prompts.  
The goal is to evaluate reasoning quality, constraint adherence, and hallucination risk — not correctness.

---

## Evaluation Checklist

For each AI response, the following behaviors are reviewed:

- Did the AI admit uncertainty when evidence was incomplete?
- Did it rank possible causes instead of guessing one?
- Did it hallucinate missing facts?
- Did it overfit on a single metric?
- Did it ignore important signals?
- Did it respect prompt constraints?

---

## Evaluation Session — Controlled Incident

### Prompt Summary

A structured incident prompt describing degraded responsiveness with elevated disk utilization and I/O wait.

---

### Observed AI Behavior

- The AI acknowledged disk pressure as a likely contributing factor.
- It referenced provided metrics rather than inventing new data.
- It ranked possible causes instead of asserting certainty.
- It indicated missing disk latency metrics.
- No hallucinated logs or system details were introduced.

---

### Strengths

- Evidence-driven reasoning
- Proper uncertainty acknowledgment
- Constraint adherence
- Multi-cause consideration

---

### Weaknesses / Risks

- Slight bias toward common disk bottleneck patterns
- Limited discussion of alternative explanations

---

### Hallucination Check

No fabricated metrics or logs were observed.

---

### Signal Handling Review

- Disk pressure recognized ✔
- CPU utilization interpreted correctly ✔
- Log context acknowledged ✔

---

## Lessons Learned

- Structured prompts significantly reduce speculative reasoning.
- Explicit constraints improve uncertainty reporting.
- Summarized metrics prevent noise-driven hallucination.

---

## Prompt Improvement Ideas

- Strengthen requirement for alternative cause ranking
- Explicitly request signal correlation reasoning
- Encourage explicit evidence referencing

---

## Summary

The AI demonstrated controlled reasoning behavior under structured prompts.  
While bias toward common failure patterns exists, constraint design effectively limits hallucination.

Prompt engineering remains essential for safe AI-assisted incident analysis.
