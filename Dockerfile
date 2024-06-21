# Use the official Python image from the Docker Hub
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache mariadb-connector-c-dev build-base mariadb-dev
    
# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

RUN apk --no-cache add mysql-dev gcc

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run Migrations
RUN python manage.py migrate

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]