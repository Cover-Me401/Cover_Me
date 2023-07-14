import pytest
import sys, os

from pathlib import Path
from dotenv import load_dotenv
dotenv_path = Path('../../.env')
load_dotenv(dotenv_path)

from .indeed import parse_search_page, _add_url_parameter, scrape_search, parse_job_page, scrape_jobs 
 





def test_parse_search_page():
    assert parse_search_page

def test__add_url_parameter():
    assert _add_url_parameter

def test_scrape_search():
    assert scrape_search

def test_parse_job_page():
    assert parse_job_page

def test_scrape_jobs():
    assert scrape_jobs

if __name__ == "__main__":
    pytest.main()
