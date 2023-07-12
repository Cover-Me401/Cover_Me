from rich.console import Console
from rich.prompt import Prompt
import os, sys, shutil
from GPT_writer import openai
from Docker.modules.resume_reader import open_resume
from Docker.modules.GPT_writer import generate_cover_letter


console = Console()
prompt = Prompt()

def program_start():
    job_title = prompt.ask("Enter a job title to search for")
    city = prompt.ask("Enter a city to search for jobs in")

    resume_path = 'Docker/modules/LoganR_Resume.pdf'
    resume_text = open_resume(resume_path).read()
    cover_letter = generate_cover_letter(resume_text)

    console.print(f"Searching for job title: {job_title}")
    console.print(f"Searching in city: {city}")
    console.print(f"Generated Cover Letter:\n{cover_letter}")

if __name__ == "__main__":
  # This line calls the `program_start()` function.
  program_start()
