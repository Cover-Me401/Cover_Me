import pytest
import sys, os
import unittest
from unittest.mock import MagicMock
from .cover_letter_generator import generate_cover_letter
import openai
import re
import unittest
import json
from .resume_reader import open_resume


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

class MockChoice:
    def __init__(self, text):
        self.text = text

class MockResponse:
    def __init__(self, choices):
        self.choices = choices

class TestGenerateCoverLetter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This is a mock response, similar to the actual OpenAI API response
        cls.mock_response = MockResponse([
            MockChoice("mock cover letter text")
        ])

    def test_generate_cover_letter(self):
        # Create a mock for openai.Completion.create
        openai.Completion.create = MagicMock(return_value=self.mock_response)

        resume_text = "resume text"
        job_description = "job description"
        expected_cover_letter = self.mock_response.choices[0].text  # this is where we adjust to use attribute instead of dictionary key

        result = generate_cover_letter(resume_text, job_description)

        # Check if the function is called with the correct arguments
        openai.Completion.create.assert_called_with(
            engine="text-davinci-003",
            prompt="Write a cover letter for the job with the following information:\n\nResume Text: {}\n\nJob Description: {}".format(resume_text, job_description),
            max_tokens=500,
            temperature=0.7,
            top_p=0.9,
        )
        # Check if the result matches the expected result
        self.assertEqual(result, expected_cover_letter)

def test_get_descriptions():
  assert get_descriptions



def get_descriptions():
  descriptions = []
  with open('Docker/modules/indeed_scraper/results/jobs.json', 'r') as file:
    job_details = file.read()
    parsed_job_details = json.loads(job_details)
    length_jobs = len(parsed_job_details)
  for i in range(length_jobs):
    description = parsed_job_details[i]['description']
    descriptions.append(description)
  return descriptions[:2]  # Return only the first 2 descriptions

def striphtml(json_details):
    p = re.compile(r'<.*?>')
    return p.sub('', json_details)

class TestStripHTML(unittest.TestCase):
    def test_striphtml_removes_tags(self):
        # Test case where HTML tags are present
        json_details = '<p>This is <b>bold</b> and <i>italic</i> text.</p>'
        expected_output = 'This is bold and italic text.'
        self.assertEqual(striphtml(json_details), expected_output)

    def test_striphtml_no_tags(self):
        # Test case where no HTML tags are present
        json_details = 'This is a plain text without any HTML tags.'
        expected_output = 'This is a plain text without any HTML tags.'
        self.assertEqual(striphtml(json_details), expected_output)

    def test_striphtml_empty_string(self):
        # Test case with an empty string
        json_details = ''
        expected_output = ''
        self.assertEqual(striphtml(json_details), expected_output)

    def test_striphtml_nested_tags(self):
        # Test case with nested HTML tags
        json_details = '<p>This is <b>bold and <i>italic</i></b> text.</p>'
        expected_output = 'This is bold and italic text.'
        self.assertEqual(striphtml(json_details), expected_output)
    


def test_open_resume():
    """
    Tests the `open_resume()` function.
    """
    filename = "A.pdf"
    expected_text = "a\n"

    with open(filename, "rb") as f:
        text = open_resume(f)

    assert text == expected_text


if __name__ == "__main__":
    test_open_resume()

if __name__ == "__main__":
    unittest.main()


test_add_url_parameter()

def test_scrape_search():
    assert scrape_search

def test_parse_job_page():
    assert parse_job_page

def test_scrape_jobs():
    assert scrape_jobs

if __name__ == "__main__":
    pytest.main()
