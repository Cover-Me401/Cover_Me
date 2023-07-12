# FIRST 
# user prompts program to start
# CLI prompts user job title to search, city to search and user responds
from rich.console import Console
from rich.prompt import Prompt
import os, sys, shutil
from BARD_writer import bard
from resume_reader import open_resume

console = Console()
prompt = Prompt()

# This function gets the user's input for the job title and city.
def program_start():
  job_title = prompt.ask("Enter a job title to search for")
  city = prompt.ask("Enter a city to search for jobs in")

  # This line calls the `resume_to_bard()` function and passes the job title and city as arguments.
  # response = resume_to_bard(job_title, city)

  # This line prints the job title and city to the console.
  console.print(f"Searching for job title: {job_title}")
  console.print(f"Searching in city: {city}")

# This function opens the user's resume file and extracts the text.
def resume_to_bard():
    text = open_resume('Docker/modules/LoganR_Resume.pdf').read()
    data = {"text": text}
    response = bard.create_response(data)
    return response

if __name__ == "__main__":
  # This line calls the `program_start()` function.
  program_start()
  resume_to_bard()
