# Notes App

A full-stack notes-taking web application built with Flask and SQLAlchemy. Users can create an account, log in securely, and manage their own private notes.

## Features

- User authentication — sign up, log in, log out
- Passwords securely hashed (never stored in plain text)
- Session-based login using Flask-Login
- Create and view personal notes
- Delete notes instantly without a page reload (via Fetch API)
- Each user's notes are private and tied only to their own account

## Tech Stack

- **Backend:** Python, Flask
- **Database / ORM:** SQLAlchemy, SQLite
- **Authentication:** Flask-Login, Werkzeug (password hashing)
- **Frontend:** HTML, CSS, JavaScript (Fetch API)

## Project Structure
website/
├── init.py      # App factory, extension setup (db, login manager)
├── auth.py          # Login, logout, sign-up routes (Blueprint)
├── views.py         # Home page, note creation/deletion routes (Blueprint)
├── models.py         # User and Note database models
├── static/
│   └── index.js      # Frontend JS (delete note via Fetch API)
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   └── sign_up.html
main.py                # Entry point — runs the app


## How It Works

- The app uses Flask's **application factory pattern** (`create_app()`), keeping setup modular and avoiding circular imports.
- Routes are organized using **Blueprints** — authentication routes and note-related routes are kept in separate files.
- User and Note data are modeled with SQLAlchemy, linked via a foreign key (`Note.user_id → User.id`), so each user only ever sees their own notes.
- Note creation happens through a standard form submission; note deletion is handled asynchronously — the frontend sends a JSON request via `fetch()`, and the backend responds without reloading the page.

## Setup & Installation

1. Clone the repository
```bash
   git clone <your-repo-url>
   cd notes-app
```

2. Create and activate a virtual environment
```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install flask flask-sqlalchemy flask-login
```

4. Run the app
```bash
   python main.py
```

5. Visit `http://127.0.0.1:5000` in your browser

## Future Improvements

- Note editing (currently only create/delete)
- Migrate from SQLite to PostgreSQL for production use
- Add note timestamps display in the UI
- Input validation and better error handling on the frontend
