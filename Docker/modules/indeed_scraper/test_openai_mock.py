import unittest
from unittest.mock import MagicMock
from Docker.modules.indeed_scraper.cover_letter_generator import generate_cover_letter
import openai

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


if __name__ == "__main__":
    unittest.main()
