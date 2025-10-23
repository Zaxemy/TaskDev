# TaskDev

A modern task management API built with FastAPI, featuring user authentication and task CRUD operations.

## Features

- **User Authentication**: JWT-based authentication with user registration and login
- **Task Management**: Full CRUD operations for tasks
- **User-specific Tasks**: Each user can only access their own tasks
- **Modern Tech Stack**: FastAPI, SQLAlchemy, PostgreSQL, Alembic migrations
- **Docker Support**: Easy deployment with Docker Compose
- **Testing**: Comprehensive test suite with pytest

## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy (async)
- **Authentication**: FastAPI-Users with JWT
- **Migrations**: Alembic
- **Testing**: pytest with async support
- **Containerization**: Docker & Docker Compose

## Project Structure

```
TaskDev/
├── api/                    # API routes
│   └── tasks.py           # Task endpoints
├── core/                  # Core application logic
│   ├── authentication/   # Auth configuration
│   ├── Dependencies/     # Dependency injection
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   └── types/            # Custom types
├── crud/                 # Database operations
│   └── tasks.py          # Task CRUD operations
├── alembic/              # Database migrations
├── tests/                # Test files
├── main.py               # Application entry point
├── compose.yaml          # Docker Compose configuration
└── pyproject.toml        # Project dependencies
```

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/jwt/login` - Login and get JWT token
- `POST /auth/jwt/logout` - Logout

### Users
- `GET /users/me` - Get current user profile
- `PATCH /users/me` - Update current user profile

### Tasks
- `GET /tasks/` - Get all tasks for current user
- `POST /tasks/` - Create a new task
- `GET /tasks/{task_id}/` - Get specific task
- `PATCH /tasks/{task_id}/` - Update a task
- `DELETE /tasks/{task_id}/` - Delete a task

## Getting Started

### Prerequisites

- Python 3.13+
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TaskDev
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql+asyncpg://postgres:12345@localhost:5432/taskdev
   ```

### Running with Docker Compose (Recommended)

1. **Start the services**
   ```bash
   docker-compose up -d
   ```

2. **Run database migrations**
   ```bash
   docker-compose exec web alembic upgrade head
   ```

3. **Access the API**
   - API: http://localhost:7777
   - Interactive docs: http://localhost:7777/docs
   - Database: localhost:5432

### Running Locally

1. **Start PostgreSQL database**
   ```bash
   docker-compose up -d db
   ```

2. **Run migrations**
   ```bash
   alembic upgrade head
   ```

3. **Start the development server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 7777
   ```

## Database Migrations

The project uses Alembic for database migrations:

```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

## Testing

Run the test suite:

```bash
# Install test dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=.
```

## API Usage Examples

### Register a User
```bash
curl -X POST "http://localhost:7777/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

### Login
```bash
curl -X POST "http://localhost:7777/auth/jwt/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"
```

### Create a Task
```bash
curl -X POST "http://localhost:7777/tasks/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README and API docs",
    "is_complete": false
  }'
```

### Get All Tasks
```bash
curl -X GET "http://localhost:7777/tasks/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Development

### Code Style
The project follows Python best practices and uses:
- Type hints throughout
- Async/await patterns
- Pydantic for data validation
- SQLAlchemy for database operations

### Adding New Features
1. Create database models in `core/models/`
2. Add Pydantic schemas in `core/schemas/`
3. Implement CRUD operations in `crud/`
4. Create API endpoints in `api/`
5. Add tests in `tests/`
6. Update migrations if needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For questions or issues, please open an issue on the GitHub repository.
