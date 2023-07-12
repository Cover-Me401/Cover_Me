import openai
import os

openai.api_key = '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'

messages = [{"role": "system", "content": "You are a helpful assistant"}]

while question := input("> "):
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(f'response: {completion["choices"][0]["message"]["content"]}')

print(completion)