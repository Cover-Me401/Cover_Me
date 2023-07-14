import pytest
import sys, os

from pathlib import Path
from dotenv import load_dotenv
dotenv_path = Path('../../.env')
load_dotenv(dotenv_path)

from .indeed import parse_search_page, _add_url_parameter, scrape_search, parse_job_page, scrape_jobs 

def test_parse_search_page():
    assert parse_search_page


def test_add_url_parameter():
    # Test case 1: Add a single parameter to the URL
    url = "https://example.com/page?param1=value1"
    updated_url = _add_url_parameter(url, param2="value2")
    expected_url = "https://example.com/page?param1=value1&param2=value2"
    assert updated_url == expected_url, f"Test case 1 failed: {updated_url}"

    # Test case 2: Replace an existing parameter value
    url = "https://example.com/page?param1=value1"
    updated_url = _add_url_parameter(url, param1="new_value")
    expected_url = "https://example.com/page?param1=new_value"
    assert updated_url == expected_url, f"Test case 2 failed: {updated_url}"

    # Test case 3: Add multiple parameters
    url = "https://example.com/page"
    updated_url = _add_url_parameter(url, param1="value1", param2="value2")
    expected_url = "https://example.com/page?param1=value1&param2=value2"
    assert updated_url == expected_url, f"Test case 3 failed: {updated_url}"

    # Test case 4: URL with existing parameters and fragments
    url = "https://example.com/page?param1=value1#fragment"
    updated_url = _add_url_parameter(url, param2="value2")
    expected_url = "https://example.com/page?param1=value1&param2=value2#fragment"
    assert updated_url == expected_url, f"Test case 4 failed: {updated_url}"

    print("All test cases passed successfully!")

test_add_url_parameter()

def test_scrape_search():
    assert scrape_search

def test_parse_job_page():
    assert parse_job_page

def test_scrape_jobs():
    assert scrape_jobs

if __name__ == "__main__":
    pytest.main()
