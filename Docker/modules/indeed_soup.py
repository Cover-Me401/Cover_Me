# SECOND
# code takes in the user input from program_start and runs BeautifulSoup on indeed using HTML reference code, including job title, city, URL, job requirements, and job description to posting.
# Code writes data to txt files

from selenium import webdriver
# from selenium.webdriver.opera.options import Options as OperOptions
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
# import program_start
import random
import json
from urllib.parse import urlencode
import re

user_agents_list = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

r = requests.get('https://www.indeed.com/jobs?', headers=user_agents_list)
print(r.text)


def get_indeed_search_url(keyword, location, offset=0):
  parameters = {'q': keyword, 'l': location, 'filter': 0, 'start': offset}
  url = 'https://www.indeed.com/jobs?' + urlencode(parameters)
  
  
  soup = BeautifulSoup(html_content, 'html.parser')
  cards = soup.find_all('div', 'cardOutline tapItem dd-privacy-allow result job_b8f6807751984821 sponsoredJob resultWithShelf sponTapItem desktop vjs-highlight css-kyg8or eu4oa1w0')
  
  
  
  
  parameters = {'q': keyword, 'l': location, 'filter': 0, 'start': offset}
  print('https://www.indeed.com/jobs?' + urlencode(parameters))
  url = 'https://www.indeed.com/jobs?' + urlencode(parameters)
  response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
  soup = BeautifulSoup(response.content, 'html.parser')  
  return cards + urlencode(parameters)







  # print(soup.text)
  title_span = soup.find_all('span')
  # print(title_span)
  # return 'https://www.indeed.com/jobs?' + urlencode(parameters)

job_id_list = []
job_url_list = []

keyword_list = ['software engineer']
location_list = ['Washington']

for keyword in keyword_list:
  for location in location_list:
    for offset in range(0, 100, 10):
      try:
        indeed_jobs_url = get_indeed_search_url(keyword, location, offset=0)
        response = requests.get(indeed_jobs_url, headers=user_agents_list)
        print('this is response', response)

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
  get_indeed_search_url('software developer', 'Seattle, WA', 0)