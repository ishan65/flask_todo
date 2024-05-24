# Use an official Python runtime as a parent image
FROM python:3.9-slim

VOLUME /usr/src/app
# Set the working directory in the container
WORKDIR /usr/src/app
COPY . .
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements_dev.txt
# Make port 5789 available to the world outside this container
EXPOSE 5789

