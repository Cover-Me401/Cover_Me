import json
from pathlib import Path
import asyncio
from rich.prompt import Prompt
from loguru import logger as log
import openai
from dotenv import load_dotenv
import os
from resume_reader import open_resume
from cover_letter_generator import generate_cover_letter
from run import run

prompt = Prompt()
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


async def program_start_async():
    job_title = prompt.ask("Enter a job title to search for")
    city = prompt.ask("Enter a city to search for jobs in")

    # Run the Indeed scraper asynchronously
    await run(job_title, city)

    # Wait for the jobs.json file to be created
    while not Path("results/jobs.json").exists():
        await asyncio.sleep(1)  # Adjust the delay as needed

    job_description = await get_job_description()

    if job_description:
        resume_text = open_resume("LoganR_Resume.pdf")

        if resume_text:
            cover_letter = generate_cover_letter(resume_text, job_description)
            output_folder = Path("Resume_Covered")
            output_folder.mkdir(exist_ok=True)
            cover_letter_file = output_folder / "cover_letter.txt"
            with open(cover_letter_file, "w") as f:
                f.write(cover_letter)
            print(f"Searching for job title: {job_title}")
            print(f"Searching in city: {city}")
            print(f"Generated Cover Letter:\n{cover_letter}")
            print(f"Cover letter saved in: {cover_letter_file}")
        else:
            print("Error: Unable to open the resume file.")
    else:
        print("Error: Unable to get the job description.")


async def get_job_description():
    """
    Get the job description from the Indeed scraping results.
    """
    # Load the job description from the JSON file
    job_description_file = Path("results/jobs.json")  # Update with the correct path

    # Wait for the file to be created
    while not job_description_file.exists():
        await asyncio.sleep(1)  # Adjust the delay as needed

    with open(job_description_file) as file:
        data = json.load(file)

    # Extract the job description from the scraping results
    job_description = data[0]["description"]  # Assuming the first job in the list, you can modify this accordingly

    return job_description


async def main():
    await program_start_async()


if __name__ == "__main__":
    asyncio.run(main())