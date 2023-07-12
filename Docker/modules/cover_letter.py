import fitz
import requests
from rich.console import Console
from rich.prompt import Prompt
from bs4 import BeautifulSoup
import openai
import time
from Docker.modules.indeed_scraper.run import run
import json
from pathlib import Path
import asyncio
import sys
sys.path.append("Docker/modules/indeed_scraper") 

openai.api_key = 'PUT YOUR OPENAI_API_KEY HERE'
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

BASE_CONFIG = {
    # Indeed.com requires Anti Scraping Protection bypass feature.
    "asp": True,
    "country": "US",
}


async def program_start():
    # Check rate limiting
    if not check_rate_limit():
        console.print("Rate limit exceeded. Please try again later.")
        return




    try:
        # Check timeout for fetching ai-plugin.json/openapi.yaml
        fetch_start_time = time.time()
        response = requests.get('https://httpbin.org/delay/2', timeout=FETCH_TIMEOUT)
        fetch_end_time = time.time()

        if fetch_end_time - fetch_start_time > FETCH_TIMEOUT:
            console.print("Fetching ai-plugin.json/openapi.yaml timed out.")
            return

        # Run the Indeed scraper asynchronously
        await run()

        # Wait for the jobs.json file to be created
        while not Path("results/jobs.json").exists():
            await asyncio.sleep(1)  # Adjust the delay as needed

        # Get the job description from Indeed using the scraped data
        job_description = get_job_description()

        # Generate the cover letter
        cover_letter = generate_cover_letter(resume_text, job_description)

        console.print(f"Searching for job title: {job_title}")
        console.print(f"Searching in city: {city}")
        console.print(f"Generated Cover Letter:\n{cover_letter}")
    except requests.exceptions.Timeout:
        console.print("A timeout occurred. Please try again later.")


def open_resume(filename):
    """
    Opens a PDF file and returns a file object.
    """
    return fitz.open(filename)



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
    # Run the asyncio event loop
    asyncio.run(program_start())

