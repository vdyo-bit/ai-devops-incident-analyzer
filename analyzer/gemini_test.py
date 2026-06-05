from google import genai
import os

client = genai.Client(
    api_key=os.environ["GOOGLE_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what OOMKilled means in Kubernetes."
)

print(response.text)
