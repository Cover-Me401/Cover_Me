import fitz
import pytest
import tempfile
import os

# assuming the open_resume function is in a file named my_module.py
from .resume_reader import open_resume

def test_open_resume():
    # create a temporary pdf file
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tf:
        doc = fitz.open(tf.name)  # Open the temporary file
        page = doc.new_page()
        page.insert_text([0, 0], "Hello World")
        doc.save(tf.name)
        temp_filename = tf.name

    try:
        # ensure our function reads the text correctly
        assert open_resume(temp_filename) == "Hello World"
    finally:
        # cleanup: remove the temporary file
        os.remove(temp_filename)

