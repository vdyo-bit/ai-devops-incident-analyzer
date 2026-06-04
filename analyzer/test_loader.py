from incident_loader import load_incident
from ai_prompt_builder import build_prompt

incident = load_incident("../incidents/cpu_saturation.json")

prompt = build_prompt(incident)

print(prompt)
