from openai import OpenAI
from ai_prompt_builder import build_prompt

client = OpenAI()

prompt = build_prompt()
print(prompt)
response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("\n===== AI RESPONSE =====\n")
print(response.output_text)

