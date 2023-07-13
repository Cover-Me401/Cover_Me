import os
import dotenv
import bardapi
from bardapi import Bard
from resume_reader import text
from dotenv import load_dotenv
import time

# set your __Secure-1PSID value to key
def bard():
  load_dotenv()
  token = os.environ['_BARD_API_KEY']
  
  bard = Bard(timeout=30) # Set timeout in seconds

  # # print(bard.get_answer("Write a cover letter for this resume:\n" + text)['content'])
  # # set your __Secure-1PSID value to key
  # token = '_BARD_API_KEY'

  # # set your input text
  # input_text = "Write a cover letter for this resume:\n" + text

  # # Send an API request and get a response.
  # response = bardapi.core.bard(token).get_answer(input_text)
  token = '_BARD_API_KEY'
  bard = Bard(token=token)
  bard.get_answer("Write a cover letter for this resume:\n" + text)['content']


if __name__ == "__main__":
  bard()
