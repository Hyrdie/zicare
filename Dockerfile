# Use the official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /zicare

# Copy the requirements file into the container at /app
COPY requirements.txt /zicare/

# Create a virtual environment
RUN python -m venv env

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY app /zicare/app

RUN mkdir logs

EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]