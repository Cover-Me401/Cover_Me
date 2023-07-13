import os
from dotenv import load_dotenv
import openai
import json
import re

def get_descriptions():
  descriptions = []
  with open('Docker/modules/indeed_scraper/results/jobs.json', 'r') as file:
    job_details = file.read()
    parsed_job_details = json.loads(job_details)
    length_jobs = len(parsed_job_details)
  for i in range(length_jobs):
    description = parsed_job_details[i]['description']
    descriptions.append(description)
  return descriptions

def striphtml(json_details):
  p = re.compile(r'<.*?>')
  return p.sub('', json_details)

def gpt():
  load_dotenv()
  openai.api_key = os.environ['OPENAI_API_KEY']
  messages = [{"role": "system", "content": "You are a helpful assistant"}]
  
  user_experience = input('Enter your work experience: ')
  descriptions = get_descriptions()
  question = f'write me a cover letter using {user_experience} and the following job descriptions: '
  for description in descriptions:
    messages.append({"role": "user", "content": question})
    messages.append({"role": "assistant", "content": description})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(f'response: {completion["choices"][0]["message"]["content"]}')
  print(completion)
  

if __name__ == "__main__":
  gpt()