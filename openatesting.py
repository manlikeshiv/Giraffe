import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=input()
)

print(response)