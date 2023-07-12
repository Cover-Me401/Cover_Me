import fitz
import requests
from rich.console import Console
from rich.prompt import Prompt
from bs4 import BeautifulSoup
import openai

console = Console()
prompt = Prompt()

def program_start():
    job_title = prompt.ask("Enter a job title to search for")
    city = prompt.ask("Enter a city to search for jobs in")

    resume_path = 'Docker/modules/LoganR_Resume.pdf'
    resume_text = open_resume(resume_path).get_toc()

    # Scrape the information from Indeed
    indeed_url = f"https://www.indeed.com/jobs?q={job_title}&l={city}"
    response = requests.get(indeed_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the job description from Indeed
    job_description = soup.find("div", class_="jobsearch-jobDescription")

    # Generate the cover letter
    cover_letter = generate_cover_letter(resume_text, job_description)

    console.print(f"Searching for job title: {job_title}")
    console.print(f"Searching in city: {city}")
    console.print(f"Generated Cover Letter:\n{cover_letter}")

def open_resume(filename):
    """
    # Opens a PDF file and returns a file object.
    """
    return fitz.open(filename)

# def generate_cover_letter(resume_text, job_description):
#     """
#     # Generate a cover letter using OpenAI and the scraped information from Indeed.
#     """
#     # Ask OpenAI to generate a cover letter
#     cover_letter = openai.generate_text(
#         prompt="Write a cover letter for the job with the following information:",
#         max_tokens=500,
#         temperature=0.7,
#         top_p=0.9,
#         input_prompts=[resume_text, job_description],
#     )

#     return cover_letter
def generate_cover_letter(resume_text, job_description):
    """
    Generate a cover letter using OpenAI and the scraped information from Indeed.
    """
    # Ask OpenAI to generate a cover letter
    prompt = "Write a cover letter for the job with the following information:\n\nResume Text: {}\n\nJob Description: {}".format(
        resume_text, job_description
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        top_p=0.9,
    )

    cover_letter = response.choices[0].text.strip()

    return cover_letter

if __name__ == "__main__":
  # This line calls the `program_start()` function.
  program_start()