# SECOND
# code takes in the user input from program_start and runs BeautifulSoup on indeed using HTML reference code, including job title, city, URL, job requirements, and job description to posting.
# Code writes data to txt files

import requests
from bs4 import BeautifulSoup
# import program_start
import requests
import json
from urllib.parse import urlencode
import re

def get_indeed_search_url(keyword, location, offset=0):
  parameters = {'q': keyword, 'l': location, 'filter': 0, 'start': offset}
  return 'https://www.indeed.com/jobs?' + urlencode(parameters)

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}

job_id_list = []
job_url_list = []

keyword_list = ['software engineer']
location_list = ['Washington']

for keyword in keyword_list:
  for location in location_list:
    for offset in range(0, 1010, 10):
      try:
        indeed_jobs_url = get_indeed_search_url(keyword, location, offset)
        response = requests.get(indeed_jobs_url, headers=headers)

        if response.status_code == 200:
          script_tag = re.findall(r'window.indeed.jobMap\]=(\{.+?\});', response.text)
          if script_tag is not None:
            json_blob = json.loads(script_tag[0])
            jobs_list = json_blob['jobs']
            for index, job in enumerate(jobs_list):
              if job.get('jobkey') is not None:
                job_id_list.append(job.get('jobkey'))
              job_url = job.get('url')
              match = re.search(r'apply-url="(.+?)"', job_url)
              if match:
                job_url_list.append(match.group(1))
            if len(jobs_list) < 10:
              break
      except Exception as e:
        print('Error', e)

print(job_id_list)
print(job_url_list)

# def get_indeed_search_url(keyword, location, offset=0):
#   parameters = {'q': keyword, 'l': location, 'filter': 0, 'start': offset}
#   return 'https://www.indeed.com/jobs?' + urlencode(parameters)

# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}

# job_id_list = []

# keyword_list = ['software engineer']
# location_list = ['Washington']

# for keyword in keyword_list:
#   for location in location_list:
#     for offset in range(0, 1010, 10):
#       try:
#         indeed_jobs_url = get_indeed_search_url(keyword, location, offset)
#         response = requests.get(indeed_jobs_url, headers=headers)

#         if response.status_code == 200:
#           script_tag = re.findall(r'window.indeed.jobMap\]=(\{.+?\});', response.text)
#           if script_tag is not None:
#             json_blob = json.loads(script_tag[0])
#             jobs_list = json_blob['jobs']
#             for index, job in enumerate(jobs_list):
#               if job.get('jobkey') is not None:
#                 job_id_list.append(job.get('jobkey'))
#             if len(jobs_list) < 10:
#               break
#       except Exception as e:
#         print('Error', e)

# print(job_id_list)






if __name__ == "__main__":
  # job_postings = get_job_postings("software engineer")
  # for job_posting in job_postings:
  #   print(job_posting)
  get_indeed_search_url('software developer', 'Washington', 0)