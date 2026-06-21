# API Explanation

## Responsible

Maryam – API & Request System

## Purpose

This document explains how the LocalLend API works, how JSON is used, and how the request workflow is implemented.

---

## What is an API?

API stands for Application Programming Interface.

An API allows different parts of an application to communicate with each other.

In the LocalLend project, the API provides data about items and lending requests.

Instead of returning a normal web page, the API returns JSON data.

---

## What is JSON?

JSON stands for JavaScript Object Notation.

JSON is a structured format used to exchange data between the backend and the frontend.

Example:

```json
{
  "id": 1,
  "name": "Bohrmaschine",
  "status": "available"
}
```

The object contains information about an item.

---

## Frontend and Backend

The frontend is the part that the user sees and interacts with.

Examples:

- Buttons
- Forms
- Pages
- Navigation

The backend works in the background.

Examples:

- Flask application
- API endpoints
- Data processing
- Request management

The frontend requests data from the backend.

The backend processes the request and returns a JSON response.

---

## How Data Flows Through the System

The complete process works as follows:

```text
User
↓
Frontend
↓
API Endpoint
↓
Flask Backend
↓
JSON Response
↓
Frontend displays the data
```

Example:

1. The user opens the LocalLend website.
2. The frontend requests data from an API endpoint.
3. Flask receives the request.
4. The corresponding function is executed.
5. The data is converted into JSON.
6. The JSON response is sent back.
7. The frontend displays the information.

---

## What jsonify() Does

The Flask function `jsonify()` converts Python data into a JSON response.

Example:

```python
return jsonify({
    "success": True,
    "message": "Items loaded successfully",
    "data": items
})
```

The response contains:

- success
- message
- data

This creates a standardized API response.

---

## Request Workflow

The request workflow describes how lending requests are processed.

### Step 1

A borrower creates a request.

Status:

```text
pending
```

### Step 2

The lender reviews the request.

### Step 3

The lender accepts the request.

Status:

```text
accepted
```

### Step 4

The lender can also reject the request.

Status:

```text
rejected
```

### Step 5

A request can be removed.

Status:

```text
deleted
```

---

## Status Values

| Status | Description |
|----------|----------|
| pending | Request created and waiting for a decision |
| accepted | Request accepted |
| rejected | Request rejected |
| deleted | Request deleted |
| available | Item available for borrowing |

---

## Implemented API Endpoints

| Endpoint | Purpose |
|----------|----------|
| /api/items | Returns available items |
| /api/requests | Returns all requests |
| /api/create_request | Creates a new request |
| /api/accept_request | Accepts a request |
| /api/reject_request | Rejects a request |
| /api/delete_request | Deletes a request |
| /api/status | Returns API information |

---

## Technologies Used

- Python
- Flask
- JSON
- Git
- GitHub

---

## My Contribution

As part of the API & Request System, I contributed the following:

- Created API endpoints
- Provided JSON responses
- Implemented request management
- Implemented request creation
- Implemented request acceptance
- Implemented request rejection
- Implemented request deletion
- Implemented status management
- Tested API endpoints
- Created API documentation
- Documented the request workflow
- Explained the API architecture and JSON usage

---

## Conclusion

The LocalLend API provides structured JSON data through multiple endpoints.

The API manages lending requests, status values, and item information.

The implementation demonstrates how frontend and backend communicate using JSON and Flask.