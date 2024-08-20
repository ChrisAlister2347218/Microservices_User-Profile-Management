
# User Profile Microservice

This repository contains a microservice for managing user profiles. The service provides a RESTful API with basic CRUD (Create, Read, Update, Delete) operations. It is built using Flask and connected to a PostgreSQL database. The project is containerized using Docker and Docker Compose.

## Project Structure

- `app/__init__.py`: Contains the Flask application factory function `create_app()` and initializes the SQLAlchemy instance.
- `app/models.py`: Defines the `User` model for the database.
- `app/routes.py`: Contains route definitions for user management.
- `run.py`: Entry point for running the Flask application.
- `Dockerfile`: Defines the Docker image for the Flask microservice.
- `docker-compose.yml`: Defines the Docker Compose configuration for running the microservice and the PostgreSQL database.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd user-profile-service1
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

1. **Start the application using Docker Compose:**

   ```bash
   docker-compose up
   ```

   This command will build the Docker images and start the containers for the microservice and the PostgreSQL database.

2. **Access the API:**

   - The Flask microservice will be available at `http://127.0.0.1:5000`.

## API Endpoints

- **GET /**: Returns a welcome message.
- **POST /users**: Create a new user profile.
  - Request body: `{ "username": "string", "email": "string", "password": "string" }`
- **GET /users/<id>**: Retrieve a user profile by ID.
- **PUT /users/<id>**: Update a user profile by ID.
  - Request body: `{ "username": "string", "email": "string", "password": "string" }`
- **DELETE /users/<id>**: Delete a user profile by ID.

## Development

To contribute to the development:

1. **Make changes to the code.**
2. **Run tests to ensure everything is working correctly.**
3. **Submit a pull request with a clear description of the changes.**

## Docker

### Dockerfile

The `Dockerfile` creates an image for the Flask microservice. It includes the following steps:

1. Use a Python base image.
2. Install dependencies.
3. Copy the application code into the image.
4. Define the entry point to start the Flask application.

### Docker Compose

The `docker-compose.yml` file sets up two services:

1. **app**: The Flask microservice.
2. **db**: The PostgreSQL database.

Both services are configured to communicate with each other.

## Documentation and Presentation

- **Documentation**: The README file provides an overview of the project, setup instructions, and API usage.
- **Presentation**: A slide deck summarizing the project, its features, challenges, and solutions is available in the `presentation` directory.

## Troubleshooting

If you encounter issues:

1. **Ensure that Docker and Docker Compose are installed and running.**
2. **Check the Docker container logs for errors.**
3. **Verify that the Flask application and PostgreSQL database are properly configured.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

