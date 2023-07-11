# FOURTH
# Code takes user input from prompts AND the job txt files and runs it through imported AI (bard) to create a cover letter that gets written to a new txt file

from bardapi import Bard

import os
from dotenv import load_dotenv
from Bard import Chatbot
from Docker.modules.resume_reader import text
import sys
# import program_start

def bard():
  # This line loads the environment variables from the .env file.
  load_dotenv()
  # This line gets the BARD API key from the environment variables.
  token = os.getenv('_BARD_API_KEY')
  # This line creates a Chatbot object with the BARD API key.
  bot = Chatbot(token)
  # This line asks the BARD API the question "who let dogs out?"
  question = bot.ask(f'Write a cover letter for this resume:\n{text}')['content']
  # question = bot.ask(f'Write a function that add 2 numbers together')['content']
  # This line prints the question.
  print(question)



if __name__ == "__main__":
  bard()