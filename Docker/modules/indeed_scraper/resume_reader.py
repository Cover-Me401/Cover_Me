# This file uses the import fitz to open a resume as PDF file and extracts the text to be added to the AI prompt.

import fitz

def open_resume(filename):
    """
    Opens a PDF file and extracts the text from it.
    """
    with fitz.open(filename) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text
