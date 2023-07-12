# FIRST 
# user prompts program to start
# CLI prompts user job title to search, city to search and user responds
from rich.console import Console
from rich.prompt import Prompt
from Docker.modules.BARD_writer import generate_cover_letter
from Docker.modules.resume_reader import open_resume

console = Console()
prompt = Prompt()

def program_start():
    job_title = prompt.ask("Enter a job title to search for")
    city = prompt.ask("Enter a city to search for jobs in")

    cover_letter = resume_to_bard()

    console.print(f"Searching for job title: {job_title}")
    console.print(f"Searching in city: {city}")
    console.print(f"Generated Cover Letter:\n{cover_letter}")

def resume_to_bard():
    resume_path = 'Docker/modules/LoganR_Resume.pdf'
    resume_text = open_resume(resume_path).read()
    cover_letter = generate_cover_letter(resume_text)
    return cover_letter

if __name__ == "__main__":
    program_start()
