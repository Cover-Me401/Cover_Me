import pytest
from Docker.modules.program_start import program_start
import io
from unittest.mock import patch

# Testing for program_start
def test_program_start():
    expected_job_title = "Software Engineer"
    expected_city = "San Francisco"

    # Simulate user input for testing
    with patch("builtins.input", side_effect=[expected_job_title, expected_city]):
        captured_output = io.StringIO()
        console.print = captured_output.write

        # Call the program_start() function
        program_start()

        # Verify the inputs
        output = captured_output.getvalue()
        assert expected_job_title in output
        assert expected_city in output


# Testing for resume_to_bard
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


# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])