# This file is an experiment to see if we can import and use "resume" through Python to bring in a user's resume file

import fitz

# This function takes a filename and a mode as input, and returns a file object. The mode can be "rb" (read binary) or "r" (read).
def open_resume(filename, mode="rb"):
    """
    # Opens a PDF file and returns a file object.
    """
    return open(filename, mode)

# This line opens the PDF file "Logan Reese - Resume (4).pdf" in read binary mode. The file object is stored in the variable `file`.
file = open_resume("Docker/modules/LoganR_Resume.pdf", "rb")

# This line creates a PDF reader object from the file object `file`.
reader = fitz.open(file)

# This line loads the first page of the PDF file into a page object. The page object is stored in the variable `page1`.
page1 = reader.load_page(0)

# This line prints the number of pages in the PDF file.
# print(reader.page_count)

# This line extracts the text from the first page of the PDF file and stores it in the variable `text`.
text = page1.get_text()

# This line prints the text from the first page of the PDF file.
# print(text)
