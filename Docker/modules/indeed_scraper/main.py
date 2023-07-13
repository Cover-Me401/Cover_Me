import asyncio
from rich.prompt import Prompt
from pathlib import Path
from resume_reader import open_resume
from program_start import program_start_async
from GPT_writer import gpt
from run import run

prompt = Prompt()

async def main():
    job_specification = prompt.ask("Enter the job role: ")
    location = prompt.ask("Enter the location: ")

    await run(job_specification, location)  # Run the Indeed scraper
    await gpt()  # Generate the cover letters

if __name__ == "__main__":
    asyncio.run(main())


