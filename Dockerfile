# Use a Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the application code into the container
COPY . /app/

# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Expose ports
EXPOSE 80

# Command to run the Flask application with NGINX
CMD ["bash", "-c", "service nginx start && gunicorn --bind 0.0.0.0:80 app:app"]
