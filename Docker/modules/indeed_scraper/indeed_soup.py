"""
This is an example web scraper for indeed.com used in scrapfly blog article:
https://scrapfly.io/blog/how-to-scrape-indeedcom/

To run this scraper set env variable $SCRAPFLY_KEY with your scrapfly API key:
$ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
"""
# import json
# import math
# import os
# import re
# from typing import Dict, List
# import urllib

# from loguru import logger as log
# from scrapfly import ScrapeApiResponse, ScrapeConfig, ScrapflyClient, ScrapflyScrapeError

# SCRAPFLY = ScrapflyClient(key=os.environ["SCRAPFLY_KEY"])
# BASE_CONFIG = {
#     # Indeed.com requires Anti Scraping Protection bypass feature.
#     "asp": True,
#     "country": "US",
# }


# def parse_search_page(result):
#     """Find hidden web data of search results in Indeed.com search page HTML"""
#     # This function uses the `re` module to find a specific pattern in the HTML of the search page.
#     # The pattern is a JSON object that contains the data for the search results.
#     # The function then returns the JSON object.

#     data = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', result.content)
#     data = json.loads(data[0])
#     return {
#         "results": data["metaData"]["mosaicProviderJobCardsModel"]["results"],
#         "meta": data["metaData"]["mosaicProviderJobCardsModel"]["tierSummaries"],
#     }


# def _add_url_parameter(url, **kwargs):
#     """Add or replace GET parameters in a URL"""
#     # This function takes a URL and a dictionary of key-value pairs, and returns a new URL with the
#     # key-value pairs added as GET parameters.

#     url_parts = list(urllib.parse.urlparse(url))
#     query = dict(urllib.parse.parse_qsl(url_parts[4]))
#     query.update(kwargs)
#     url_parts[4] = urllib.parse.urlencode(query)
#     return urllib.parse.urlunparse(url_parts)


# async def scrape_search(url: str, max_results: int = 1000) -> List[Dict]:
#     """Scrape Indeed.com search for job listing previews"""
#     # This function scrapes the Indeed.com search page for job listing previews.
#     # It takes a URL and a maximum number of results as input, and returns a list of dictionaries
#     # containing the data for the job listing previews.

#     log.info(f"scraping search: {url}")
#     result_first_page = await SCRAPFLY.async_scrape(ScrapeConfig(url, **BASE_CONFIG))
#     data_first_page = parse_search_page(result_first_page)

#     results = data_first_page["results"]
#     total_results = sum(category["jobCount"] for category in data_first_page["meta"])
#     # There's a page limit on indeed.com of 1000 results per search.
#     # If the maximum number of results is greater than 1000, then we only scrape the first 1000 results.

#     if total_results > max_results:
#         total_results = max_results

#     print(f"scraping remaining {(total_results - 10) / 10} pages")
#     other_pages = [
#         ScrapeConfig(_add_url_parameter(url, start=offset), **BASE_CONFIG)
#         for offset in range(10, total_results + 10, 10)
#     ]
#     log.info("found total pages {} search pages", math.ceil(total_results / 10))
#     async for result in SCRAPFLY.concurrent_scrape(other_pages):
#         if not isinstance(result, ScrapflyScrapeError):
#             data = parse_search_page(result)
#             results.extend(data["results"])
#         else:
#             log.error(f"failed to scrape {result.api_response.config['url']}, got: {result.message}")
#     return results


# def parse_job_page(result: ScrapeApiResponse):
#     """parse job data from job listing page"""
#     # This function parses the data from a job listing page on Indeed.com.
#     # It takes a ScrapeApiResponse object as input, and returns a dictionary containing the data for the job listing.

#     data = re.findall(r"_initialData=(\{.+?\});", result.content)
#     data = json.loads(data[0])
#     data = data["jobInfoWrapperModel"]["jobInfoModel"]
#     return {
#         "description": data['sanitizedJobDescription']['content'],
#         data["jobMetadataHeaderModel"],
#         (data["jobTagModel"])
#     }
#------------------------------CODE ABOVE IS FROM INDEED SCRAPING 2023 GITHUB-------------------------------------------
# SECOND
# code takes in the user input from program_start and runs BeautifulSoup on indeed using HTML reference code, including job title, city, URL, job requirements, and job description to posting.
# Code writes data to txt files


import requests
from bs4 import BeautifulSoup
from modules.program_start import program_start
import random
import json
from urllib.parse import urlencode
import re
from datetime import datetime
import csv

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

  response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
  else:
    return None



def get_indeed_search_url(keyword, location, offset=0):
  parameters = {'q': keyword, 'l': location, 'filter': 0, 'start': offset}
  url = 'https://www.indeed.com/jobs?' + urlencode(parameters)
  
  
  soup = BeautifulSoup(response.content, 'html.parser')
  cards = soup.find_all('div', 'cardOutline tapItem dd-privacy-allow result job_b8f6807751984821 sponsoredJob resultWithShelf sponTapItem desktop vjs-highlight css-kyg8or eu4oa1w0')
  

  parameters = {'q': keyword, 'l': location, 'filter': 0, 'start': offset}
  print('https://www.indeed.com/jobs?' + urlencode(parameters))
  url = 'https://www.indeed.com/jobs?' + urlencode(parameters)
  response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
  soup = BeautifulSoup(response.content, 'html.parser')  
  return cards + urlencode(parameters)


  print(soup.text)
  title_span = soup.find_all('span')
  print(title_span)
  return 'https://www.indeed.com/jobs?' + urlencode(parameters)

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



if __name__ == "__main__":
  job_postings = get_job_postings("software engineer")
  for job_posting in job_postings:
    print(job_posting)
  get_indeed_search_url('software developer', 'Seattle, WA', 0)




# -------------------------------------



def get_url(position, location):
	template = 'https://www.indeed.com/jobs?q={}&l={}'
	url = template.format(position, location)
	return url

url = get_url('software developer', 'seattle wa')


# extract the raw html data via get request
response = requests.get(url)
print(response) 

# should get 200 code
response.reason
# should be 'OK'

soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find_all('div', 'cardOutline')

# prototype extraction of single record

card = cards[0]
span = card.h2.a.span
job_title = span.get('title')
job_url = 'https://indeed.com' + span.get('href')
company = card.find('span', 'companyName').text.strip()
location = card.find('div', 'companyLocation').text.strip()
job_description = card.find('div', 'job-snippet').text.strip()
