# Design Decision: Password Hashing

## Metadata
| Key | Value |

| --- | --- |

| Status | Decided |

| Date | 20.06.2026 |

| Team | LocalLend – Gruppe 5 |

| Decision taken by | Tuba Celik |

## Problem Statement

Users need to register with a password. Storing passwords directly as plain text would be unsafe and bad practice.

## Decision

We decided to hash passwords before storing them.

The backend uses `generate_password_hash()` for registration and `check_password_hash()` for login.

## Regarded Options

| Option | Advantages | Disadvantages |

| --- | --- | --- |

| Plain text passwords | Easy to implement | Unsafe and not professional |

| Password hashing | More secure and standard practice | Slightly more complex |

| External authentication service | Very advanced | Too complex for current project scope |

## Reasoning

Password hashing is a realistic and secue solution for our prototype. It improves the quality of the backend without making the project too complex.

## Consequences

Passwords are not stored directly in readable form. Login still works because the entered password can be checked against the stored hash.

## Proof

- app.py

- `generate_password_hash()`

- `check_password_hash()`

- Commit: Add login and register backend