import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlencode
import re

def get_zip_recruiter_search_url(keyword, location):
    params = {
        "q": keyword,
        "where": location,
    }
    encoded_params = urlencode(params)

    search_url = "https://www.monster.com/jobs/search/?{}".format(encoded_params)

    return search_url

def get_job_posting_url(search_url):
    """This function gets the job posting URL from a Monster search URL.

    Args:
        search_url (str): The Monster search URL.

    Returns:
        str: The job posting URL.
    """

    # This line makes a request to the Monster search page.
    response = requests.get(search_url)

    # This line parses the HTML response from Monster.
    soup = BeautifulSoup(response.content, "html.parser")

    # This line finds the job posting URL in the HTML.
    job_posting_url = soup.find("li", class_="sc-gcUDKN cSkSaC").get("href")


if __name__ == "__main__":
    search_url = get_monster_search_url("python developer", "seattle")
    job_posting_url = get_job_posting_url(search_url)
    print(job_posting_url)
