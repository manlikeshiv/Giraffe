from openai import OpenAI
import os

#os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()
OpenAI.api_key = "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"
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chat_log = []

while True:
    user_message = input()
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = client_instance.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=chat_log
        )
        assistant_response = response['choices'][0]['message']['content']
        print("ChatGPT:", assistant_response.strip("\n").strip())
        chat_log.append({"role": "user", "content": assistant_response.strip("/").strip()})