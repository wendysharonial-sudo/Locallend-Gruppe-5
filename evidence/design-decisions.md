# Design Decisions

## Overview

This document records the most important design decisions made during the development of **LocalLend**.

LocalLend is a Flask-based web application that enables users to lend and borrow tools and technical devices within their local community.

The purpose of this document is to explain not only **what** was implemented, but also **why** specific technical and product decisions were made.

Each design decision includes:

- the problem that needed to be solved
- the selected solution
- alternative options that were considered
- the trade-offs of each option
- the consequences of the final decision

---

# DD-01: Provide Item and Request Data Through a JSON API

## Meta Information

| Field | Value |
|---|---|
| Status | Decided |
| Updated | 23-Jun-2026 |
| Team | LocalLend |
| Lead | Maryam |

## Problem Statement

LocalLend manages item listings and lending requests.

Users and system components require access to structured information about available items and request states. The project also requires at least one headless API endpoint that returns data in JSON format.

The team therefore had to decide whether item and request data should only be displayed through HTML pages or also be exposed through a structured JSON API.

## Decision

We decided to provide selected item and request data through a JSON API.

JSON is structured, machine-readable and independent from the HTML layout. This makes the data easier to test, document and reuse. It also fulfils the project requirement of providing a headless API endpoint.

**Decision Owner:** Maryam

## Options Considered

| Criterion | HTML Pages Only | JSON API |
|---|---|---|
| Human readability | Easy to read in the browser | Not designed as a visual page |
| Structured data access | Data is mixed with HTML | Data is clearly structured |
| Project requirement | Does not fulfil the JSON API requirement | Fulfils the JSON API requirement |
| Testing | Harder to test separately | Easier to test through API endpoints |
| Documentation | Harder to document as an interface | Endpoints and responses can be documented clearly |
| Future extensibility | Limited | Strong |

## Consequences

### Positive

- Meets the JSON API project requirement
- Enables structured data exchange
- Makes testing and debugging easier
- Supports future frontend integration

### Negative

- Additional endpoints must be maintained
- API responses need separate documentation

---

# DD-02: Manage Lending Requests Through Status Values

## Meta Information

| Field | Value |
|---|---|
| Status | Decided |
| Updated | 23-Jun-2026 |
| Team | LocalLend |
| Lead | Maryam |

## Problem Statement

Lending requests move through multiple stages during their lifecycle.

A newly created request is open first. Afterwards, the lender can either accept or reject it. The application therefore needs a clear way to represent the current state of each request.

The team had to decide whether handled requests should disappear after a decision or remain visible with a status value.

## Decision

We decided to manage lending requests through status values.

A new request starts with the status `pending`. If the lender accepts the request, the status changes to `accepted`. If the lender rejects the request, the status changes to `rejected`. A request can also be marked as `deleted`.

This makes the request process transparent, understandable and easier to explain.

**Decision Owner:** Maryam

## Options Considered

| Criterion | Delete Requests After Handling | Store Request Status |
|---|---|---|
| Simplicity | Less data remains visible | Requires an additional status value |
| Traceability | Hard to see what happened later | Request history remains understandable |
| User understanding | Request may suddenly disappear | User can see the current state |
| Request workflow | No clear lifecycle | Clear lifecycle from pending to accepted/rejected |
| Debugging | Harder to check previous states | Easier to inspect the current state |

## Consequences

### Positive

- Clear request lifecycle
- Better transparency for users
- Easier debugging
- Easier documentation of the workflow

### Negative

- Requires status management
- Status values must be documented consistently

---

# DD-03: Use Request-Based Lending Instead of Automatic Lending

## Meta Information

| Field | Value |
|---|---|
| Status | Decided |
| Updated | 23-Jun-2026 |
| Team | LocalLend |
| Lead | Maryam |

## Problem Statement

LocalLend focuses on tools and technical devices. These items can be valuable, fragile or personally important to their owners.

The team had to decide whether borrowers should automatically receive an item after selecting it or whether the lender should approve each borrowing request manually.

This decision is important because lenders should remain in control of who can borrow their items.

## Decision

We decided to use a request-based lending process.

Borrowers can submit a lending request, but the item is not automatically borrowed. The lender must first accept or reject the request.

This approach gives lenders more control and better fits the trust-based nature of local lending.

**Decision Owner:** Maryam

## Options Considered

| Criterion | Automatic Lending | Request-Based Lending |
|---|---|---|
| Borrowing speed | Faster for borrowers | Borrower must wait for approval |
| Lender control | Lower | Higher |
| Trust and security | Riskier for valuable items | Better for tools and technical devices |
| Request management | No accept/reject process | Clear accept/reject workflow |
| Fit for LocalLend | Too automatic for personal items | Fits local lending between people |

## Consequences

### Positive

- Greater control for lenders
- Better trust between users
- Clear approval workflow
- Better protection of valuable items

### Negative

- Borrowers must wait for approval
- Additional request management is required

---

# DD-04: Categorize Tools and Technical Devices

## Meta Information

| Field | Value |
|---|---|
| Status | Decided |
| Updated | 23-Jun-2026 |
| Team | LocalLend |
| Lead | Maryam |

## Problem Statement

Users need an easy way to find tools and technical devices.

Without categories, searching becomes difficult when many items are listed. This is especially relevant for LocalLend because items can belong to different groups such as tools, technical devices or accessories.

The team had to decide whether items should be listed without structure, grouped into fixed categories or described with flexible tags.

## Decision

We decided to use fixed categories for listed items.

Examples include:

- Tools
- Technical devices
- Accessories
- Other

Fixed categories provide a consistent structure and improve discoverability while keeping the implementation simple.

For the current prototype, simplicity and clarity are more important than maximum flexibility.

**Decision Owner:** Maryam

## Options Considered

| Criterion | No Categories | Fixed Categories | Flexible Tags |
|---|---|---|---|
| Ease of use | Low | High | Medium |
| Implementation complexity | Very low | Low | Medium |
| Consistency | Low | High | Medium |
| Search support | Low | Medium | High |
| Suitability for prototype | Low | High | Medium |
| Future extension | Limited | Can be extended later | Flexible from the start |

## Consequences

### Positive

- Easier item discovery
- Consistent item structure
- Simple implementation
- Easy for users to understand

### Negative

- Less flexible than tags
- Categories may need expansion later

---

# DD-05: Standardize API Responses Using JSON Objects

## Meta Information

| Field | Value |
|---|---|
| Status | Decided |
| Updated | 23-Jun-2026 |
| Team | LocalLend |
| Lead | Maryam |

## Problem Statement

The API provides data for items, lending requests and status information.

Without a standardized response structure, different endpoints could return data in inconsistent formats. This would make testing, debugging and documentation more difficult.

The team therefore had to decide how API responses should be structured.

## Decision

We decided to use a consistent JSON response structure for all API endpoints.

Example:

```json
{
  "success": true,
  "message": "Items loaded successfully",
  "data": []
}
```

This structure ensures that every endpoint follows the same pattern.

- `success` shows whether the request was successful.
- `message` explains what happened.
- `data` contains the actual response data.

**Decision Owner:** Maryam

## Options Considered

| Criterion | Plain Text | JSON Objects | XML |
|---|---|---|---|
| Readability | Medium | High | Medium |
| Structured data | Low | High | High |
| Flask integration | Low | High | Medium |
| API standardization | Low | High | Medium |
| Documentation | Medium | High | Medium |
| Suitability for this project | Low | High | Medium |

## Consequences

### Positive

- Consistent API behavior
- Easier testing
- Easier documentation
- Better maintainability
- Clearer communication between backend and frontend

### Negative

- All endpoints must follow the same response format

---

# Summary

The design decisions documented above focus on the most important architectural and workflow-related choices made during the development of LocalLend.

They support:

- structured API communication through JSON
- transparent request management
- trust-based lending workflows
- improved usability through categorization
- consistent and maintainable backend behavior

Together, these decisions provide a clear foundation for a scalable and understandable lending platform.