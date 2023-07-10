# THIRD
# CLI prompts user to input their professional info
# User enters years of experience, keywords from previous jobs, tech language(s), and professional interests
from rich.console import Console
from rich.prompt import Prompt
import os
import sys
import shutil


console = Console()
prompt = Prompt()

def user_professional_info():
    years_experience = Prompt.ask("Enter your years of experience in the field")
    prev_jobs_keywords = Prompt.ask("Enter some keywords from previous jobs or projects")
    tech_languages = Prompt.ask("Enter the tech language(s) you want to use")
    professional_interests = Prompt.ask("Enter some of  your professional interests")
    # call fn or do something with the inputs
    # pass variables to search fn?
    # figure out how to enter multiple keywords for all but first prompt
    console.print(f"Inputting: {years_experience}")
    console.print(f"Inputting: {prev_jobs_keywords}")
    console.print(f"Inputting: {tech_languages}")
    console.print(f"Inputting: {professional_interests}")


if __name__ == "__main__":
  user_professional_info()

