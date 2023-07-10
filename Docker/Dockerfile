# Dockerfile-blueprint for creating images, Image-template for running container, Container- runs packaged projects
# Runs top down like most files
FROM python:3.10.4 

ADD job_soup.py .

RUN pip install requests beautifulsoup4

CMD [ "python", "./job_soup.py" ]

