import os
from dotenv import load_dotenv
import openai
from modules.GPT_writer import gpt

def test_gpt_with_valid_api_key():
  load_dotenv()
  openai.api_key = "YOUR_API_KEY"
  messages = [{"role": "system", "content": "You are a helpful assistant"}]
  while question := input("> "):
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    assert completion["choices"][0]["message"]["content"] != ""

def test_gpt_with_invalid_api_key():
  load_dotenv()
  openai.api_key = "INVALID_API_KEY"
  with pytest.raises(openai.APIError):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

def test_gpt_with_no_api_key():
  load_dotenv()
  openai.api_key = None
  with pytest.raises(openai.APIError):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

if __name__ == "__main__":
  pytest.main()
