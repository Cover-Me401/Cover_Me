import pytest
from Docker.modules.resume_reader import open_resume
import fitz
import os
import io

# Testing for open_resume
# @pytest.mark.skip
def test_open_resume():
  assert open_resume() == None

# @pytest.mark.skip
def test_open_resume():
    expected_filename = "test_resume.pdf"
    expected_mode = "rb"

    # Create a temporary resume file for testing
    with open(expected_filename, "w") as file:
        file.write("Sample Resume Text")

    # Call the open_resume() function
    file_object = open_resume(expected_filename, expected_mode)

    # Verify the file object and mode
    assert isinstance(file_object, io.IOBase)
    assert file_object.mode == expected_mode

    # Clean up the temporary resume file
    os.remove(expected_filename)

# @pytest.mark.skip
def test_open_resume_missing_file():
    filename = "missing_file.pdf"
    assert open_resume(filename) == None

@pytest.mark.skip
def test_open_resume_invalid_mode():
    with pytest.raises(ValueError):
        open_resume("test_resume.pdf", "r")

@pytest.mark.skip
def test_open_resume_not_pdf():
    with pytest.raises(TypeError):
        open_resume("test_resume.txt", "rb")

@pytest.mark.skip
def test_open_resume_no_text():
    filename = "empty_resume.pdf"
    with open(filename, "w") as file:
        file.write("")
    text = open_resume(filename)
    assert text == ""


# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])



