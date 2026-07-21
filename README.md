# LocalLend

Contributors: Mariam Joumma, Tuba Celik, Wendy Sharonia Lontsi Doumtsop, Jean Yves Nkwane

# Project Description

LocalLend is a Flask-based web application for lending and borrowing everyday items within a local community.

The goal of the project is to encourage resource sharing, reduce unnecessary purchases and make it easy for users to lend and borrow items.

---

# How to run the application

## 1. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Install all dependencies

```bash
pip install -r requirements.txt
```

## 3. Start the application

macOS / Linux

```bash
python3 app.py
```

Alternative

```bash
flask run
```

Windows

```bash
python app.py
```

The application will be available at

```
http://127.0.0.1:5000
```

---

# Database

The SQLite database is created automatically on first start if it does not already exist.

If required, it can also be initialized manually:

```bash
flask init-db
```

---

# Main Features

- User registration
- User login
- Secure password hashing
- Session management
- Create lending offers
- Browse available items
- Search for items
- View item details
- Send borrowing requests
- Accept or reject requests
- Automatic item status updates
- Return borrowed items
- User profile
- JSON API endpoints

---

# Technology Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML
- CSS
- Bootstrap
- Jinja2

---

# Documentation

Additional documentation is available in the `docs` and `evidence` folders.

It includes:

- Product Discovery
- Value Proposition
- Design Decisions
- API Documentation
- API Testing
- Technical Documentation
- User Survey
- Data Model

---

# Authors

- Mariam Joumma
- Tuba Celik
- Wendy Sharonia Lontsi Doumtsop
- Jean Yves Nkwane
