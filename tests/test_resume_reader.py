import pytest
from Docker.modules.resume_reader import open_resume
import fitz

# Testing for open_resume
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

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])




def test_open_resume():
  assert open_resume() == None