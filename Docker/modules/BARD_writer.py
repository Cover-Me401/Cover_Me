import bardapi
from bardapi import Bard
import os
import dotenv
from resume_reader import text

# set your __Secure-1PSID value to key
def bard():
  load_dotenv()
  
  token = os.environ['_BARD_API_KEY']



  bard = Bard(timeout=30) # Set timeout in seconds
  bard.get_answer("Write a cover letter for this resume:\n" + text)['content']

  print(bard.get_answer("Write a cover letter for this resume:\n" + text)['content'])

if __name__ == "__main__":
  bard()
