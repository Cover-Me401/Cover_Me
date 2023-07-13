# FIFTH
# This file runs the entire program, function by function, from program start to cover letter files written
import asyncio
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from run import run
from GPT_writer import gpt

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


if __name__ == "__main__":
  job_specification = input('Enter job role: ')
  job_specification = job_specification.replace(" ", "+")
  location = input('Enter a location: ')
  asyncio.run(run(job_specification, location))
  gpt()
