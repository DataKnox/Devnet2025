# NetAuto API

A simple FastAPI application containerized with Docker.

## Running the Application

### Using Docker

1. Build the Docker image:
```bash
docker build -t netauto-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 netauto-api
```

The API will be available at http://localhost:8000

### Endpoints

- GET `/`: Welcome message
- GET `/health`: Health check endpoint

### API Documentation

Once the application is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc