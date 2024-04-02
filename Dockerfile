# Dockerfile for building a Flask application container

# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster 

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the Flask application
EXPOSE 80

# Set the command to run when the container starts
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]

