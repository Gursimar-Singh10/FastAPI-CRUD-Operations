# FastAPI CRUD Operations

A simple **Todo CRUD API** built with **FastAPI**, **SQLAlchemy**, and **MySQL**. It demonstrates how to structure a FastAPI project with a database layer, ORM models, and Pydantic schemas for request/response validation.

## Features

- Create, list, retrieve, and delete todo items
- SQLAlchemy ORM models backed by a MySQL database
- Pydantic schemas for request validation and response serialization
- Database session handling via FastAPI dependency injection
- Environment-based configuration using `python-dotenv`

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [PyMySQL](https://pymysql.readthedocs.io/) — MySQL driver
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [Uvicorn](https://www.uvicorn.org/) — ASGI server
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable loading

## Project Structure

```
FastAPI-CRUD-Operations/
├── main.py            # FastAPI app, Pydantic schemas, and CRUD routes
├── models.py           # SQLAlchemy ORM model for Todo
├── database.py          # DB engine, session, and Base setup
├── index.py             # Standalone FastAPI learning/scratch examples (not wired into main.py)
├── requirements.txt     # Python dependencies
└── .gitignore
```

> **Note:** `index.py` is a separate, self-contained file used for practicing basic FastAPI concepts (path params, query params, request bodies). It is not imported by or connected to `main.py`.

## Prerequisites

- Python 3.8+
- A running MySQL server

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Gursimar-Singh10/FastAPI-CRUD-Operations.git
   cd FastAPI-CRUD-Operations
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root with your database connection string:

   ```env
   DATABASE_URL=mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>
   ```

   Make sure the target database already exists on your MySQL server — SQLAlchemy will create the `todos` table automatically on startup.

## Running the App

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint            | Description              |
|--------|----------------------|---------------------------|
| GET    | `/todos`              | Get all todo items        |
| GET    | `/todos/{todo_id}`    | Get a single todo by ID   |
| POST   | `/todos`              | Create a new todo item    |
| DELETE | `/todos/{todo_id}`    | Delete a todo by ID       |

### Todo Schema

| Field         | Type    | Required | Default |
|---------------|---------|----------|---------|
| `title`       | string  | Yes      | —       |
| `description` | string  | No       | `null`  |
| `completed`   | boolean | No       | `false` |

### Example: Create a Todo

```bash
curl -X POST "http://127.0.0.1:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread", "completed": false}'
```

### Example: Get All Todos

```bash
curl http://127.0.0.1:8000/todos
```

## Known Limitations

- There's no `PUT`/`PATCH` endpoint to **update** an existing todo yet — a `TodoUpdate` schema is defined in `main.py` but isn't currently wired to a route.
- No authentication/authorization is implemented.
- No pagination on the `GET /todos` list endpoint.

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request — implementing the update endpoint would be a great first contribution.

## License

No license file is currently included in this repository. Consider adding one (e.g., MIT) if you intend for others to reuse this code.
