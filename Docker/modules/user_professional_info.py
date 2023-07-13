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

def user_professional_info(years_experiance, prev_jobs_keywords, tech_languages, professional_interests):
    years_experience = Prompt.ask("Enter your [bold cyan]years[/bold cyan] of experience in the field")
    prev_jobs_keywords = Prompt.ask("Enter some [bold cyan]keywords[/bold cyan] from previous jobs or projects")
    tech_languages = Prompt.ask("Enter the [bold cyan]tech language(s)[/bold cyan] you want to use")
    professional_interests = Prompt.ask("Enter some of  your [bold cyan]professional interests[/bold cyan]")
    # call fn or do something with the inputs
    # pass variables to search fn?
    # figure out how to enter multiple keywords for all but first prompt
    console.print(f"Inputting: {years_experience}", style='gold1')
    console.print(f"Inputting: {prev_jobs_keywords}", style='gold1')
    console.print(f"Inputting: {tech_languages}", style='gold1')
    console.print(f"Inputting: {professional_interests}", style='gold1')


if __name__ == "__main__":
  user_professional_info()

