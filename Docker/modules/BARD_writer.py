# import bardapi
# from bardapi import Bard
# import os
# import dotenv
# from resume_reader import text

# # set your __Secure-1PSID value to key
# def bard():
#   load_dotenv()
  
#   token = os.environ['_BARD_API_KEY']
#   bard = Bard(timeout=30) # Set timeout in seconds
#   bard.get_answer("Write a cover letter for this resume:\n" + text)['content']

#   print(bard.get_answer("Write a cover letter for this resume:\n" + text)['content'])

# if __name__ == "__main__":
#   bard()
import openai
import os

openai.api_key = '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'

messages = [{"role": "system", "content": "You are a helpful assistant"}]

while question := input("> "):
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(f'response: {completion["choices"][0]["message"]["content"]}')

print(completion)
