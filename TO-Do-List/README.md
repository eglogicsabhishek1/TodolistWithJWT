# ✅ FastAPI To-Do List with MySQL

A RESTful API built with FastAPI to manage a To-Do List, featuring full CRUD operations, JWT authentication, filtering, sorting, pagination, and database migrations with Alembic.

---

## 🚀 Features

- User Registration & JWT Login
- Create, Read, Update, Delete Tasks
- Filter by Status or Priority
- Sort by ID, Due Date, or Priority (asc/desc)
- Pagination support
- Alembic-based database migrations
- MySQL Database Integration
- Postman Collection for API testing

---

## 🏗️ Project Structure

fastapi_to_do_list/ │ ├── App/ │ ├── todo_App/ │ │ ├── init.py │ │ ├── models.py # SQLAlchemy models │ │ ├── schema.py # Pydantic models for validation │ │ ├── routes.py # Task API endpoints │ │ ├── crud.py # Business logic for DB operations │ │ ├── database.py # DB connection setup │ │ ├── auth/ │ │ │ ├── auth_routes.py │ │ │ ├── auth_handler.py │ │ │ └── auth_bearer.py │ │ └── utils/ # Optional helpers │ ├── main.py # FastAPI entrypoint ├── requirements.txt ├── .env ├── alembic.ini ├── alembic/ # Alembic migrations folder └── README.md

yaml
Copy
Edit

---

## 🧰 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **MySQL**
- **SQLAlchemy**
- **Pydantic**
- **Alembic**
- **JWT (PyJWT + PassLib)**
- **Uvicorn**

---

## 🔐 Authentication

- Register: `POST /auth/register`
- Login: `POST /auth/login` → returns JWT token
- Use the JWT token as `Bearer Token` in Authorization header for all `/tasks/` endpoints.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/fastapi_to_do_list.git
cd fastapi_to_do_list
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
⚙️ Setup .env
Create a .env file in the root with the following:

ini
Copy
Edit
DATABASE_URL=mysql+mysqlconnector://username:password@localhost/todo_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
🧪 Run the App
bash
Copy
Edit
uvicorn main:app --reload
🔄 Alembic Migrations
bash
Copy
Edit
alembic init alembic
# Update alembic/env.py and alembic.ini with your DB URL and target_metadata

alembic revision --autogenerate -m "create users and tasks table"
alembic upgrade head
📮 Postman Collection
Import the provided Postman collection (ToDoList.postman_collection.json) for testing all endpoints.

🧾 MySQL Database Setup
📌 Step 1: Create Database
sql
Copy
Edit
CREATE DATABASE todo_db;
📌 Step 2: Create Tables via SQL (if not using Alembic)
sql
Copy
Edit
-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Tasks Table
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    priority VARCHAR(20),
    due_date DATE,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);
✅ Alternatively, just run migrations via Alembic after defining your models.

📚 License
MIT

✨ Author
Abhishek Kumar – GitHub


👨‍💻 Author
Abhishek Kumar
Junior Python Developer