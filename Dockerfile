FROM python:3.10

# Define environment variable
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

RUN apt update && apt install -y python3-dev

# Install Pip and Pipenv for managing the python packages
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install pipenv

COPY ./Pipfile.lock /app/Pipfile.lock
COPY ./Pipfile /app/Pipfile

RUN pipenv install --system --dev --ignore-pipfile

COPY . .
WORKDIR /app/mysite