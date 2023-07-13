import os
from dotenv import load_dotenv
import openai
import json
import re
from resume_reader import open_resume
from cover_letter_generator import generate_cover_letter

def get_descriptions():
  descriptions = []
  with open('Docker/modules/indeed_scraper/results/jobs.json', 'r') as file:
    job_details = file.read()
    parsed_job_details = json.loads(job_details)
    length_jobs = len(parsed_job_details)
  for i in range(length_jobs):
    description = parsed_job_details[i]['description']
    descriptions.append(description)
  return descriptions[:2]  # Return only the first 2 descriptions

def striphtml(json_details):
  p = re.compile(r'<.*?>')
  return p.sub('', json_details)

async def gpt():
    load_dotenv()
    openai.api_key = os.environ['OPENAI_API_KEY']

    resume_filename = input('Enter your resume filename: ')  # Get the resume filename from the user
    user_experience = open_resume(resume_filename)  # Get the work experience from the resume

    descriptions = get_descriptions()

    for idx, description in enumerate(descriptions):
        cover_letter = generate_cover_letter(user_experience, description)  # Generate the cover letter
        print(f'Cover Letter {idx+1}: {cover_letter}\n\n')


if __name__ == "__main__":
  gpt()
