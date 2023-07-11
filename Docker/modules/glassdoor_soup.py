import requests
from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlencode
import re
import pandas as pd

def glassdoor():
  url = "https://www.indeed.com/jobs?q=python+developer&l=Seattle%2C+WA&start=0&vjk=672a66a7735e72f9"
  # response = requests.get(url)
  # print(response)
  # soup = BeautifulSoup(response.content, "html.parser")
  table = pd.read_html(url)
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')

  # print(response)
  

  # jobs = soup.find_all("li", class_="jl")

  # for job in jobs:
  #   title = job.find("div", class_="job-title mt-xsm").text
  #   location = job.find("div", class_="location mt-xxsm").text
  #   description = job.find('div', class_='jobDescriptionContent desc').text
    
  #   print("Title:", title)
  #   print("Location:", location)
  #   print("-----------")

if __name__ == '__main__':
  glassdoor()