from openai import OpenAI
from ai_prompt_builder import build_prompt
from incident_loader import load_incident

client = OpenAI()

incident = load_incident(
    "../incidents/cpu_saturation.json"
)

prompt = build_prompt(incident)

print("\n===== GENERATED PROMPT =====\n")
print(prompt)

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("\n===== AI RESPONSE =====\n")
print(response.output_text)
