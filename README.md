# Zicare: A Healthcare Reservation Microservice

Zicare is a comprehensive healthcare reservation microservice built with FastAPI, providing a robust API for managing clinics, doctors, patients, and appointments.

This microservice offers a complete solution for healthcare providers to manage their operations efficiently. It allows for the creation and management of clinics, doctors, and patients, as well as the scheduling of appointments and management of operational hours.

The system is designed with flexibility in mind, supporting various use cases such as multi-clinic setups, doctor-clinic associations, and patient management. It also includes features like queue management and reservation status tracking, making it suitable for a wide range of healthcare scenarios.

## Repository Structure

The repository is organized as follows:

- `app/`: Main application directory
  - `api/`: API route definitions
  - `orm/`: Database models and setup
  - `repository/`: Database interaction layer
  - `schema/`: Pydantic models for request/response validation
  - `service/`: Business logic layer
  - `main.py`: Application entry point
  - `settings.py`: Application configuration
- `docker-compose.yml`: Docker Compose configuration
- `Dockerfile`: Docker image definition
- `requirements.txt`: Python dependencies
- `find_sequence.py`: Utility script for linked list operations

Key files:
- `app/main.py`: Entry point for the FastAPI application
- `app/orm/db.py`: Database models definition
- `app/service/operational_hours.py`: Operational hours management
- `app/service/reservation.py`: Reservation management
- `app/api/clinic_api.py`: Clinic-related API endpoints
- `app/api/doctor_api.py`: Doctor-related API endpoints

## Usage Instructions

### Installation

Prerequisites:
- Docker and Docker Compose (version 3.8 or higher)
- Python 3.8 or higher (for local development)

To set up the project:

1. Clone the repository
2. Navigate to the project directory
3. Create a `.env` file in the `app/` directory with the necessary environment variables (see `app/sample.env` for reference)
4. Run the following command to start the services:

```bash
docker-compose up --build
```

This will start the PostgreSQL database and the FastAPI application.

### Getting Started

Once the services are up and running, you can access the API documentation at `http://localhost:8000/docs`.

The API provides endpoints for managing:
- Clinics
- Doctors
- Patients
- Operational Hours
- Reservations

### Configuration Options

The application can be configured using environment variables. Key configuration options include:
- `DATABASE_URL`: PostgreSQL connection string
- `APP_NAME`: Application name
- `LOG_LEVEL`: Logging level
- `CORS_ALLOW_ORIGINS`: Allowed origins for CORS

### Common Use Cases

1. Creating a new clinic:

```python
import requests

url = "http://localhost:8000/clinic/"
payload = {
    "name": "New Clinic",
    "address": "123 Health Street",
    "doctor_name": "Dr. Smith"
}
response = requests.post(url, json=payload)
print(response.json())
```

2. Scheduling a reservation:

```python
import requests

url = "http://localhost:8000/reservation/"
payload = {
    "clinic_id": 1,
    "doctor_id": 1,
    "patient_id": 1,
    "operational_id": 1,
    "date_time_reservation": "2023-04-01T10:00:00"
}
response = requests.post(url, json=payload)
print(response.json())
```

### Testing & Quality

To run tests (assuming you have pytest installed):

```bash
pytest app/tests
```

### Troubleshooting

Common issues and solutions:

1. Database connection errors:
   - Ensure the PostgreSQL service is running
   - Check the `DATABASE_URL` in your `.env` file
   - Verify network connectivity between the app and database containers

2. API returning 500 errors:
   - Check the application logs for detailed error messages:
     ```bash
     docker-compose logs app
     ```
   - Ensure all required environment variables are set

3. CORS issues:
   - Verify the `CORS_ALLOW_ORIGINS` setting in your `.env` file
   - Ensure your client application's origin is included in the allowed origins

For debugging:
- Set `LOG_LEVEL=DEBUG` in your `.env` file for more verbose logging
- Check the application logs in the `logs/` directory

## Data Flow

The Zicare microservice follows a layered architecture for processing requests:

1. Client sends a request to an API endpoint
2. FastAPI router handles the request and calls the appropriate service function
3. Service layer implements business logic and interacts with the repository layer
4. Repository layer performs database operations using SQLAlchemy ORM
5. Database (PostgreSQL) stores and retrieves data
6. Response flows back through the layers to the client

```
Client <-> FastAPI Router <-> Service Layer <-> Repository Layer <-> Database
```

Important technical considerations:
- The application uses SQLAlchemy for database operations
- Pydantic models are used for request/response validation
- CORS middleware is implemented for cross-origin requests
- The application uses asynchronous database operations for improved performance

## Deployment

Prerequisites:
- Docker and Docker Compose installed on the target machine
- Access to a PostgreSQL database (can be containerized or external)

Deployment steps:
1. Clone the repository on the target machine
2. Create a `.env` file with production configuration
3. Build and start the containers:
   ```bash
   docker-compose up -d --build
   ```
4. Configure a reverse proxy (e.g., Nginx) to forward requests to the application container
5. Set up SSL/TLS certificates for secure communication

Environment configurations:
- Use production-grade PostgreSQL settings
- Set appropriate logging levels and file paths
- Configure allowed origins for CORS in a production environment

Monitoring setup:
- Implement health check endpoints
- Set up logging to a centralized log management system
- Configure container and host-level monitoring

## Infrastructure

The Zicare microservice infrastructure is defined in the `docker-compose.yml` file:

- Database:
  - Type: PostgreSQL
  - Image: postgres:14.1-alpine
  - Purpose: Stores all application data

- Application:
  - Type: FastAPI
  - Image: Custom built from Dockerfile
  - Purpose: Hosts the Zicare microservice API

The `Dockerfile` defines the application container:
- Base image: python:3.8-slim
- Installs dependencies from `requirements.txt`
- Copies application code and sets up the environment
- Exposes port 8000 for the FastAPI application

The application uses environment variables for configuration, which should be defined in a `.env` file in the `app/` directory.