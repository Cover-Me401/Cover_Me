import pytest
from modules.program_start import program_start
import io
import os
from unittest.mock import patch


# Testing for program_start
# @pytest.mark.skip
def test_program_start():
    expected_job_title = "Software Engineer"
    expected_city = "San Francisco"

    # Simulate user input for testing
    with patch("builtins.input", side_effect=[expected_job_title, expected_city]):
        captured_output = io.StringIO()
        print(captured_output.write)

        # Call the program_start() function
        program_start()

        # Verify the inputs
        output = captured_output.getvalue()
        assert expected_job_title in output
        assert expected_city in output


# Testing for resume_to_bard
@pytest.mark.skip
def test_resume_to_bard():
    expected_resume_text = "Sample Resume Text"  # Replace with the expected resume text

    # Create a temporary resume file for testing
    with open("test_resume.pdf", "w") as file:
        file.write(expected_resume_text)

    # Patch the open_resume() function to return the temporary resume file
    with patch("resume_reader.open_resume", return_value=open("test_resume.pdf", "r")):
        # Call the resume_to_bard() function
        response = resume_to_bard()

        # Verify the extracted text
        assert expected_resume_text in response

    # Remove the temporary resume file
    os.remove("test_resume.pdf")


# Testing for invalid user input
@pytest.mark.skip
def test_program_start_invalid_input():
    with patch("builtins.input", side_effect=["invalid job title", "invalid city"]):
        captured_output = io.StringIO()
        console.print = captured_output.write

        # Call the program_start() function
        program_start()

        # Verify the error message
        output = captured_output.getvalue()
        assert "Invalid job title" in output
        assert "Invalid city" in output


# Testing for a missing resume file
@pytest.mark.skip
def test_resume_to_bard_missing_resume():
    # Patch the open_resume() function to return None
    with patch("resume_reader.open_resume", return_value=None):
        # Call the resume_to_bard() function
        response = resume_to_bard()

        # Verify the error message
        assert "Resume file not found" in response


# Testing for a resume file that is not a PDF
@pytest.mark.skip
def test_resume_to_bard_not_pdf():
    # Create a temporary text file
    with open("test_resume.txt", "w") as file:
        file.write("Sample Resume Text")

    # Patch the open_resume() function to return the temporary text file
    with patch("resume_reader.open_resume", return_value=open("test_resume.txt", "r")):
        # Call the resume_to_bard() function
        response = resume_to_bard()

        # Verify the error message
        assert "Resume file is not a PDF" in response


# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
