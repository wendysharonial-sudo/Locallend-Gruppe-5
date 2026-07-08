# LocalLend

Contributors: Mariam Joumma, Tuba, Wendy, Yves

## How to run application

```bash
flask run
```

## How to initialise development environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to initialise database

```bash
flask init-db
```

The command creates the SQLite database and required tables.

## Project Description

LocalLend is a web application for local lending and borrowing of items within a community.

The goal of the project is to reduce unnecessary purchases and support sustainable resource sharing. Users can create items, browse available items and manage borrowing requests.

## Main Features

- User Registration
- User Login
- User Logout
- Session Management
- Create Items
- Browse Available Items
- Borrowing Requests
- Accept Requests
- Reject Requests
- Request Status Management
- JSON API Endpoints

## Request Status

- pending
- accepted
- rejected

## Technology Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2
- JSON API

## Documentation

Additional project documentation can be found in the evidence folder.

### Included Documentation

- Product Discovery
- Design Challenge
- User Problems
- Value Proposition
- Solution Elements
- Tests
- Survey Documentation
- API Documentation
- API Explanation
- API Testing
- Design Decisions

## Team Responsibilities

### Mariam Joumma

Responsible for:

- JSON API
- API Endpoints
- Request Management
- Request Workflow
- Request Status Management
- API Documentation
- API Testing
- Product Discovery
- Survey Documentation
- Design Decisions

### Tuba

Responsible for:

- Flask Setup
- Login
- Registration
- Logout
- Sessions

### Wendy

Responsible for:

- Database Design
- SQLite Integration
- Data Model
- Database Queries
- Tables for Users, Items and Requests

### Yves

Responsible for:

- Frontend Development
- HTML Templates
- CSS Styling
- Navigation
- User Interface Testing

## Authors

- Mariam Joumma
- Tuba
- Wendy
- Yves



