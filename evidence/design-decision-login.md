# Design Decision: User Authentication with Flask Sessions

## Metadata

| Key | Value |
| --- | --- |
| Status | Decided |
| Date | 20.06.2026 |
| Team | LocalLend – Gruppe 5 |
| Decision taken by | Tuba Celik |

## Problem Statement

LocalLend needs a way to identify users during their interaction with the app.

Users should be able to register, log in and log out. After login, the application needs to remember which user is currently active.

## Decision

We decided to use Flask sessions for login state management.

After successful login, the backend stores the user id and user name in the session. During logout, the session is cleared.

## Regarded Options

| Option | Advantages | Disadvantages |
| --- | --- | --- |
| No login state | Very simple | User cannot stay logged in |
| Flask sessions | Simple, built into Flask, good for this project scope | Requires secret key |
| External authentication service | More professional | Too complex for first submission |

## Reasoning

Flask sessions fit the current scope of the project. They are easy to explain, simple to implement and enough for a first prototype.

## Consequences

The app can distinguish between logged-in and logged-out users. This supports later features such as creating items, sending requests and showing user-specific content.

## Proof

- app.py
- route `/login`
- route `/logout`
- `session["user_id"]`
- `session.clear()`