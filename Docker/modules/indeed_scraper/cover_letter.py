import fitz
import requests
from rich.console import Console
from rich.prompt import Prompt
from bs4 import BeautifulSoup
import openai
import time
from indeed_scraper.run import run
import json
from pathlib import Path
import asyncio
import sys

sys.path.append("Docker/modules/indeed_scraper/indeed.py")  # Add the path to the indeed_scraper module

# HARDCODE IN FOR NOW
openai.api_key = 'OPENAI_API_KEY'
console = Console()
prompt = Prompt()


# Variables for rate limiting
MAX_REQUESTS = 10  # Maximum number of requests allowed within the time window
TIME_WINDOW = 60  # Time window in seconds

# Variables to track rate limiting
last_request_time = 0

# Timeout thresholds
FETCH_TIMEOUT = 15  # Timeout for fetching ai-plugin.json/openapi.yaml
API_TIMEOUT = 45  # Timeout for API calls


def program_start():
    job_title = prompt.ask("Enter a job title to search for")
    city = prompt.ask("Enter a city to search for jobs in")

    resume_path = 'Docker/modules/LoganR_Resume.pdf'
    resume_text = open_resume(resume_path)
    job_description = get_job_description()

    if resume_text is not None and job_description is not None:
        cover_letter = generate_cover_letter(resume_text, job_description)

        console.print(f"Searching for job title: {job_title}")
        console.print(f"Searching in city: {city}")
        console.print(f"Generated Cover Letter:\n{cover_letter}")

        # Create the "Resume_Covered" folder if it doesn't exist
        output_folder = Path(__file__).parent / "Resume_Covered"
        output_folder.mkdir(exist_ok=True)

        # Save the cover letter in a text file
        cover_letter_file = output_folder / "cover_letter.txt"
        cover_letter_file.write_text(cover_letter)
        console.print(f"Cover letter saved in: {cover_letter_file}")
    else:
        console.print("Error: Unable to generate cover letter.")


def open_resume(filename):
    """
    Opens a PDF file and returns a file object.
    """
    try:
        with fitz.open(filename) as pdf:
            return pdf
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return None


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


def check_rate_limit():
    """
    Checks if the rate limit has been exceeded.
    """
    global last_request_time

    current_time = time.time()
    elapsed_time = current_time - last_request_time

    if elapsed_time < TIME_WINDOW:
        if requests.get('https://httpbin.org/status/429').status_code == 429:
            return False
    else:
        last_request_time = current_time

    return True


def get_job_description():
    """
    Get the job description from the Indeed scraping results.
    """
    # Load the job description from the JSON file
    job_description_file = Path("results/jobs.json")  # Update with the correct path

    # Wait for the file to be created
    while not job_description_file.exists():
        time.sleep(1)  # Adjust the delay as needed

    with open(job_description_file) as file:
        data = json.load(file)

    # Extract the job description from the scraping results
    job_description = data[0]["description"]  # Assuming the first job in the list, you can modify this accordingly

    return job_description





if __name__ == "__main__":
    # Run the program synchronously
    program_start()

    # Run the asyncio event loop
    asyncio.run(program_start_async())


