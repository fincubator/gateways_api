# Use an official Python runtime as a parent image
FROM python:3.7

RUN pip install pipenv

# Set the working directory to /app
WORKDIR /app

COPY Pipfile.lock /app

RUN pipenv install --ignore-pipfile --keep-outdated

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8080 available to the world outside this container
EXPOSE 8080
