# pip install python-docx
# pip install docx
# pip install pyresparser
# import os
# import nltk
# from pyresparser import ResumeParser

# from docx import Document

# file should be txt, docx, or pdf only

# filed=input('/Users/sarahglass/projects/courses/401/Cover_Me/Docker/modules/LoganR_Resume.pdf')
#filepath 
#/content/akshay_resume.pdf

# def pyresparser():
#   try:
#     doc = Document()
#     with open(filed, 'r') as file:
#       doc.add_paragraph(file.read())
#     doc.save("text.docx")
#     data = ResumeParser('text.docx').get_extracted_data()
#     print(data['skills'])
#   except:
#     data = ResumeParser(filed).get_extracted_data()
#     print(data['skills'])
# if you just return data, you should see everything that is returned.

# def resume_parser():
#   directory = '/Users/sarahglass/projects/courses/401/Cover_Me/Docker/modules/'
#   file = 'LoganR_Resume.pdf'
#   data=ResumeParser(directory+file).get_extracted_data()
#   return data




# if __name__ == "__main__":
#   resume_parser()