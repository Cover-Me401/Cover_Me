import re
import unittest
import json

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
    

if __name__ == '__main__':
    unittest.main()