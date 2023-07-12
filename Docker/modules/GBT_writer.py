import openai
import os

openai.api_key = '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'

messages = [{"role": "system", "content": "You are a helpful assistant"}]

while question := input("> "):
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(f'response: {completion["choices"][0]["message"]["content"]}')

print(completion)





