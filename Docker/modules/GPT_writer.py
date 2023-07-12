import os
from dotenv import load_dotenv
import openai

def gpt():
  load_dotenv()
  openai.api_key = os.environ['OPENAI_API_KEY']
  messages = [{"role": "system", "content": "You are a helpful assistant"}]
  while question := input("> "):
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(f'response: {completion["choices"][0]["message"]["content"]}')
  print(completion)

if __name__ == "__main__":
  gpt()