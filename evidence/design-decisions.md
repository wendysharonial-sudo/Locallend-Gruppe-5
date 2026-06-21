Design Decisions

Overview

This document records the most important design decisions made during the development of LocalLend.

LocalLend is a Flask-based web application that enables users to lend and borrow tools and technical devices within their local community.

The purpose of this document is to explain not only what was implemented, but also why specific technical and product decisions were made.

Each design decision includes:

* the problem that needed to be solved
* the selected solution
* alternative options that were considered
* the trade-offs of each option
* the consequences of the final decision

⸻

DD-01: Use Request-Based Lending Instead of Automatic Lending

Meta Information

Field	Value
Status	Decided
Updated	23-Jun-2026
Team	LocalLend

Problem Statement

LocalLend enables users to lend and borrow tools and technical devices.

Many items can be valuable, fragile or personally important to their owners. Therefore, the application requires a process that allows lenders to decide who may borrow their items.

The team had to decide whether borrowing should happen automatically or whether lenders should manually approve requests.

Decision

We decided to use a request-based lending process.

Borrowers can submit a lending request, but the lender must first accept or reject the request before the item can be borrowed.

This approach gives lenders more control and creates a more trustworthy lending process.

Options Considered

Criterion	Automatic Lending	Request-Based Lending
Borrowing speed	High	Medium
Lender control	Low	High
Security	Low	High
Trust between users	Medium	High
Suitability for LocalLend	Medium	High

Consequences

Positive

* Greater lender control
* Better trust between users
* Clear borrowing workflow
* Better protection of valuable items

Negative

* Borrowers must wait for approval
* Additional workflow logic is required

⸻

DD-02: Manage Lending Requests Through Status Values

Meta Information

Field	Value
Status	Decided
Updated	23-Jun-2026
Team	LocalLend

Problem Statement

Borrowing requests move through different stages during their lifecycle.

The application requires a clear way to represent the current state of each request and communicate that state to users.

The team had to decide whether handled requests should be deleted or remain visible with a status value.

Decision

We decided to manage lending requests through status values.

Each request can have one of the following states:

* pending
* accepted
* rejected
* deleted

This creates a transparent and understandable workflow.

Options Considered

Criterion	Delete Requests	Store Status Values
Simplicity	High	Medium
Transparency	Low	High
Traceability	Low	High
User understanding	Low	High
Debugging	Harder	Easier

Consequences

Positive

* Clear request lifecycle
* Better transparency for users
* Easier debugging
* Easier documentation

Negative

* Additional status management is required
* Status values must remain consistent

⸻

DD-03: Use Fixed Categories for Item Classification

Meta Information

Field	Value
Status	Decided
Updated	23-Jun-2026
Team	LocalLend

Problem Statement

Users need an efficient way to find items.

As the number of listings increases, browsing becomes more difficult without a clear structure.

The team had to decide whether items should be displayed without categories, organized through fixed categories or described through tags.

Decision

We decided to use fixed categories.

Examples include:

* Tools
* Technical Devices
* Accessories
* Other

Fixed categories provide a consistent structure and simplify navigation.

Options Considered

Criterion	No Categories	Fixed Categories	Tags
Simplicity	High	High	Medium
Consistency	Low	High	Medium
Searchability	Low	Medium	High
Implementation effort	Low	Low	Medium
Suitability for prototype	Medium	High	Medium

Consequences

Positive

* Easier item discovery
* Better navigation
* Consistent item organization
* Simple implementation

Negative

* Less flexible than tags
* Categories may require expansion in the future

⸻

DD-04: Require User Authentication for Lending Actions

Meta Information

Field	Value
Status	Decided
Updated	23-Jun-2026
Team	LocalLend

Problem Statement

LocalLend involves interactions between real users who lend and borrow personal items.

The platform requires accountability and protection against misuse.

The team had to decide whether visitors should be allowed to create listings and requests anonymously or whether authentication should be required.

Decision

We decided that users must be authenticated before creating listings or borrowing requests.

This improves accountability, ownership and trust.

Options Considered

Criterion	Guest Access	Authentication Required
Ease of access	High	Medium
Accountability	Low	High
Security	Low	High
Trust	Low	High
Suitability for LocalLend	Medium	High

Consequences

Positive

* Better accountability
* Reduced misuse
* Clear ownership of listings and requests
* Increased trust between users

Negative

* Users must register and log in
* Authentication functionality must be maintained

⸻

DD-05: Use SQLite for Data Persistence

Meta Information

Field	Value
Status	Decided
Updated	23-Jun-2026
Team	LocalLend

Problem Statement

LocalLend needs to store users, items and lending requests permanently.

The team had to select a database solution that is easy to set up, maintain and use during development.

Decision

We decided to use SQLite.

SQLite does not require a separate database server and can easily be executed locally.

This makes it well suited for a university project and simplifies installation for examiners.

Options Considered

Criterion	SQLite	PostgreSQL
Setup effort	Low	Medium
Local development	Easy	Medium
Scalability	Medium	High
Prototype suitability	High	Medium
Maintenance effort	Low	Medium

Consequences

Positive

* Easy setup
* Fast development
* No external database server required
* Simple local execution

Negative

* Limited scalability
* Migration may be necessary in larger systems

⸻

DD-06: Use Flask Templates Instead of a Separate React Frontend

Meta Information

Field	Value
Status	Decided
Updated	23-Jun-2026
Team	LocalLend

Problem Statement

LocalLend requires a user interface that allows users to browse items, create lending requests and manage their activities.

The team had to decide whether the frontend should be implemented using Flask templates with server-side rendering or through a separate React frontend connected to an API.

For the current project, simplicity and maintainability were important factors.

Decision

We decided to use Flask templates with Jinja instead of a separate React frontend.

This keeps the frontend and backend inside one application and reduces overall complexity.

It also makes the application easier to run locally because no additional frontend build process is required.

Options Considered

Criterion	Flask Templates	React Frontend
Development effort	Low	High
Setup complexity	Low	High
Learning curve	Low	High
Local reproducibility	Easy	Medium
Project suitability	High	Medium
Flexibility	Medium	High

Consequences

Positive

* Simpler project structure
* Faster implementation
* Easier local setup
* Easier maintenance
* Well suited for the project scope

Negative

* Less interactive than a modern single-page application
* Frontend and backend are more tightly coupled

⸻

Summary

The documented design decisions explain the most important architectural and product-related choices behind LocalLend.

The decisions cover:

* lending workflow
* request lifecycle
* item classification
* user authentication
* database selection
* frontend architecture

Together, these decisions provide a clear explanation of why the system was designed in its current form and how the selected solutions support the goals of the project.