# Todo Application

A full-stack CRUD Todo web application featuring a high-performance RESTful API and a dynamic templated frontend. This project demonstrates secure user authentication, robust database management, and seamless backend-to-frontend integration.

## Tech Stack

* **Backend Framework:** FastAPI 
* **Data Validation:** Pydantic v2
* **Frontend:** Jinja2 templates, HTML, CSS, JavaScript
* **Database:** SQLAlchemy ORM with SQLite (Development) / PostgreSQL (Production)
* **Security:** JWT (JSON Web Token) authentication and route protection
* **Testing:** Pytest integration test suites

## Local Setup

**1. Activate your virtual environment:**
```bash
# Windows
fastapienv\Scripts\activate

# macOS/Linux
source fastapienv/bin/activate
```

**2. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the FastAPI development server:**
```bash
uvicorn main:app --reload
```

**4. Access the application:**
Open your browser to `http://127.0.0.1:8000` and the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Testing

**Execute the integration test suite using pytest:**
```bash
pytest
```

## Production Deployment (PostgreSQL)

To deploy this application using a PostgreSQL database instead of the local SQLite development database:

**1. Install the PostgreSQL driver:**
Ensure `psycopg2-binary` (or your preferred Postgres driver) is installed on the production server.
```bash
pip install psycopg2-binary
```

**2. Configure the Environment:**
Set your production database connection string in your environment variables (or `.env` file):
```env
SQLALCHEMY_DATABASE_URL="postgresql://username:password@hostname:port/database_name"
```

**3. Database Initialization:**
Ensure your deployment script connects to the PostgreSQL instance and generates the necessary tables before launching the Uvicorn worker.