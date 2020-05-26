# Use an official Python runtime as a parent image
FROM python:3.7

RUN pip install pipenv

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install env

RUN pipenv install

# Make port 8080 available to the world outside this container
EXPOSE 8080
