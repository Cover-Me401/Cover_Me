import os
import dotenv
import bardapi
from bardapi import Bard
from Docker.modules.resume_reader import text
from dotenv import load_dotenv
import time

# set your __Secure-1PSID value to key
def bard():
  load_dotenv()
  
  token = os.environ['_BARD_API_KEY']
  bard = Bard(timeout=30) # Set timeout in seconds
  bard.get_answer("Write a cover letter for this resume:\n" + text)['content']

  print(bard.get_answer("Write a cover letter for this resume:\n" + text)['content'])

if __name__ == "__main__":
  bard()
