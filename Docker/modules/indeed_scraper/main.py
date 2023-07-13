import asyncio
from rich.prompt import Prompt
from pathlib import Path
from GPT_writer import gpt
from run import run

prompt = Prompt()

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)

async def main():
    # Get job role and location from user
    job_specification = prompt.ask("Enter the job role").replace(" ", "+")
    location = prompt.ask("Enter the location")

    await run(job_specification, location)  # Run the Indeed scraper

    await gpt()  # Generate the cover letters

if __name__ == "__main__":
    asyncio.run(main())

