# AI Guardrails

## Goal

Prevent unsafe AI recommendations.

## Current Rules

- No command execution
- No service shutdown suggestions
- No process termination recommendations

## Why

AI analysis is advisory only.
Human validation is always required.

## Future Improvements

- Detect overconfidence
- Detect unsupported conclusions

## Overconfidence Detection

The analyzer flags language that implies certainty
without sufficient evidence.

Examples:

- definitely
- certainly
- guaranteed
- 100%

## Additional Safety Controls

- AI recommendations are advisory only
- AI outputs are validated before report generation
- Missing evidence must be explicitly reported
- Confidence must be proportional to evidence quality

## Human Review Requirement

AI-generated conclusions must be reviewed by an engineer before operational decisions are made.

The goal is to encourage probabilistic reasoning.
