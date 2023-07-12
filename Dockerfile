# Build image: docker build -t <image_name> .

FROM python:3
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# SET WORK DIR
WORKDIR /Docker


# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install dependacies not covered by requirements.txt one at a time here

# Copy project
COPY . .
