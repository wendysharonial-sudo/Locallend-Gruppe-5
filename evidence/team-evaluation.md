---
title: Team Evaluation
layout: default
nav_order: 6
has_children: false
---

# Team Evaluation

## Goals

### General Project Goals

| Goal | Status |
|---|---|
| Develop a functional application for local lending and borrowing | Achieved |
| Implement user registration, login and session management | Achieved |
| Store users, items and requests using SQLite | Achieved |
| Create a structured lending request workflow | Achieved |
| Provide JSON API endpoints | Achieved |
| Create a user-friendly interface | Achieved |
| Gain practical experience with Flask, SQLite and web development | Achieved |

### Individual Goals

#### Tuba

- Improve backend development skills with Flask – Achieved
- Learn how authentication and sessions work – Achieved
- Gain experience with user management systems – Achieved

#### Wendy

- Improve database design skills – Achieved
- Learn how SQLite integrates with Flask – Achieved
- Gain experience designing data models – Achieved

#### Yves

- Improve frontend development skills – Achieved
- Gain experience with HTML, CSS and Jinja templates – Achieved
- Improve usability and interface design skills – Achieved

#### Maryam

- Improve API development skills – Achieved
- Learn how JSON APIs are implemented in Flask – Achieved
- Gain experience documenting technical decisions and workflows – Achieved

### Missed Goals

No major project goals were missed. All core requirements were successfully implemented.

---

## Improvements

- Use SQLAlchemy instead of direct SQLite queries for a cleaner database architecture.
- Improve the separation between authentication, item management and request management.
- Add more automated tests for the API and application workflows.
- Improve mobile responsiveness and accessibility.
- Add additional search and filtering features for items.
- Improve deployment and continuous integration workflows.

---

## Peer Review

### [Tuba] – Review about Wendy

#### My observation (Wahrnehmung)

Wendy worked reliably on the database and data model. She designed the structure for users, items and requests and ensured that the relationships between the tables were understandable and functional.

#### Effect on me (Wirkung)

Her work provided a stable foundation for the project and made it easier for the team to implement additional functionality.

#### Tip for the future (Wunsch)

I encourage Wendy to continue her structured approach and to take an even larger role in database architecture decisions in future projects.

---

### [Wendy] – Review about Yves

#### My observation (Wahrnehmung)

Yves was responsible for the frontend and user interface. He worked on HTML pages, CSS styling, navigation and template design. He consistently improved the usability of the application.

#### Effect on me (Wirkung)

His work made the application easier to use and helped create a more professional appearance.

#### Tip for the future (Wunsch)

I encourage Yves to continue developing his frontend skills and to explore additional UI frameworks and design techniques.

---

### [Yves] – Review about Maryam

#### My observation (Wahrnehmung)

Maryam was responsible for the API and lending request workflow. She implemented JSON endpoints, request handling logic and API documentation. She also contributed significantly to the project documentation.

#### Effect on me (Wirkung)

Her work ensured that the core lending functionality worked correctly and that technical decisions were clearly documented.

#### Tip for the future (Wunsch)

I encourage Maryam to continue taking initiative in architecture and documentation and to further deepen her API development skills.

---

### [Maryam] – Review about Tuba

#### My observation (Wahrnehmung)

Tuba was responsible for the backend foundation and authentication system. She implemented registration, login, logout and session handling. She ensured that authenticated user functionality worked reliably throughout the application.

#### Effect on me (Wirkung)

Her work provided a solid backend foundation and made it possible to connect application features to specific users.

#### Tip for the future (Wunsch)

I encourage Tuba to continue expanding her backend development skills and to take on more architecture-related responsibilities in future projects.

---

## Contributions

### Tuba – Backend & Login

**Responsibility:** `app.py`

**Tasks**

- Flask setup
- Login
- Registration
- Logout
- Session management

**Explainable Contribution**

Tuba can explain how authentication works, how users log in and how Flask routes are structured.

---

### Wendy – Database & Data Model

**Responsibility:** SQLite and data model

**Tasks**

- Users table
- Items table
- Requests table
- Data model creation
- Database queries
- SQLite integration

**Explainable Contribution**

Wendy can explain how data is stored, how the tables are connected and how database queries are performed.

---

### Yves – Frontend & User Interface

**Responsibility:** `templates/` and `static/`

**Tasks**

- HTML pages
- CSS design
- Navigation
- Jinja2 templates
- Frontend testing
- Frontend bug fixing

**Explainable Contribution**

Yves can explain the structure of the user interface, page navigation and template rendering.

---

### Maryam – API & Request System

**Responsibility:** JSON API and request logic

**Tasks**

- API endpoints
- JSON responses
- Lending request management
- Create requests
- Accept requests
- Reject requests
- Status management: `pending`, `accepted`, `rejected`
- API documentation
- API testing
- Workflow documentation

**Explainable Contribution**

Maryam can explain how data is exposed through the API, how JSON is used and how the lending request workflow is implemented.

---

## Sources

- LocalLend project repository
- LocalLend project documentation
- Flask documentation
- SQLite documentation
- GitHub documentation