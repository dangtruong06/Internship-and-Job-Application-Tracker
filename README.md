# Appli — Job & Internship Tracker

A full-stack web app for tracking job and internship applications. Built with Flask, PostgreSQL, and Bootstrap 5.

---

## Features

- **Authentication** — register, log in, and log out securely with hashed passwords via bcrypt
- **Dashboard** — view all your applications at a glance with status counts and a sortable jobs table
- **Full CRUD** — add, edit, and delete job applications
- **Status tracking** — track each application through Applied, Interview, Phone Screen, and Rejected stages
- **Per-user data** — each user only sees their own applications
- **Responsive dark UI** — high-contrast dark theme built with Bootstrap 5

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Flask |
| Database | PostgreSQL, SQLAlchemy 2.0 |
| Auth  | Flask-Login, bcrypt |
| Forms | Flask-WTF |
| Frontend | Jinja2, Bootstrap 5, Bootstrap Icons |

---

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL running locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/internship-tracker-app.git
cd internship-tracker-app
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and set the following:

```
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://username:password@localhost:5432/your_db_name
```

### 5. Set up the database

Open a Python shell and create the tables:

```bash
python3
```

```python
from main import app, db
with app.app_context():
    db.create_all()
```

### 6. Run the app

```bash
python3 main.py
```

Visit `http://localhost:5000` in your browser.

---

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Flask secret key for session signing |
| `DATABASE_URL` | PostgreSQL connection string |

A `.env.example` file is included in the repo with placeholder values.

---

## Screenshots

> Add screenshots here once the app is deployed or finalized.
<img width="1701" height="963" alt="Screenshot 2026-06-29 at 10 16 47 AM" src="https://github.com/user-attachments/assets/67e5e064-3c91-429b-90ba-7d649a40fa6d" />


