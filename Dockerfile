# Use a Python base image
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy files
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

# Expose the port the backend will run on
EXPOSE 8000

# Start the backend server
CMD ["python", "backend/main.py"]
