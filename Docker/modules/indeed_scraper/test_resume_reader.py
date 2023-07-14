import fitz
import pytest
import tempfile
import os

# assuming the open_resume function is in a file named my_module.py
from .resume_reader import open_resume

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
