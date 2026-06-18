# Design Decisions

## 01: Provide item and request data through a JSON API

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

### Problem statement

LocalLend is a Flask web application for borrowing and lending tools and technical devices.

The app has two main user roles: lenders and borrowers. Lenders offer items such as tools or technical devices. Borrowers search for available items and send lending requests.

The project requires at least one headless API endpoint that delivers data as JSON. Therefore, we had to decide whether item and request data should only be shown on HTML pages or also be provided through a structured JSON API.

### Decision

We decided to provide selected item and request data through a JSON API.

JSON is structured, machine-readable and independent from the HTML layout. This also fulfils the mandatory requirement of providing at least one headless API endpoint.

*Decision was taken by:* Maryam

### Regarded options

We regarded two options:

+ Show data only through HTML pages.
+ Provide selected data through a JSON API.

| Criterion | HTML pages only | JSON API |
| --- | --- | --- |
| **Human users** | ✔️ Easy to read in the browser | ❌ Not meant as a visual page |
| **Structured data** | ❌ Data is mixed with HTML | ✔️ Data is clearly structured |
| **Project requirement** | ❌ Does not fulfil the JSON API requirement | ✔️ Fulfils the JSON API requirement |
| **Documentation** | ❌ Harder to describe as an interface | ✔️ Endpoint and response can be documented clearly |

---

## 02: Manage lending requests through status values

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

### Problem statement

Borrowers can send lending requests for tools and technical devices.

A request does not end immediately after it is created. First, it is open. Then the lender can either accept or reject it. The app therefore needs a clear way to represent the current state of each request.

We had to decide whether handled requests should be deleted or whether they should remain stored with a status value.

### Decision

We decided to keep lending requests in the database and manage them through status values.

A new request starts with the status `pending`. If the lender accepts the request, the status changes to `accepted`. If the lender rejects the request, the status changes to `rejected`.

This makes the request process easier to understand, explain and debug.

*Decision was taken by:* Maryam

### Regarded options

We regarded two options:

+ Delete requests after they are handled.
+ Keep requests and update their status.

| Criterion | Delete handled requests | Store request status |
| --- | --- | --- |
| **Simplicity** | ✔️ Less data remains stored | ❌ Requires an additional status field |
| **Traceability** | ❌ Hard to see what happened later | ✔️ Request history remains visible |
| **User understanding** | ❌ Request may suddenly disappear | ✔️ User can see pending, accepted or rejected |
| **Request workflow** | ❌ No clear lifecycle | ✔️ Clear lifecycle from pending to accepted/rejected |

---

## 03: Use request-based lending instead of automatic lending

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

### Problem statement

LocalLend focuses on tools and technical devices. These items can be valuable, fragile or personally important to the lender.

We had to decide whether borrowers should be able to borrow an item automatically or whether the lender should first approve each request.

This decision is important because lenders should keep control over who borrows their tools or technical devices.

### Decision

We decided to use request-based lending.

Borrowers can send a lending request, but the item is not automatically borrowed. The lender must accept or reject the request.

This decision gives lenders more control and fits the focus on tools and technical devices, because these items often require trust and careful handling.

*Decision was taken by:* Maryam

### Regarded options

We regarded two options:

+ Automatic lending after a borrower clicks on an item.
+ Request-based lending with lender approval.

| Criterion | Automatic lending | Request-based lending |
| --- | --- | --- |
| **Speed** | ✔️ Faster for borrowers | ❌ Borrower must wait for approval |
| **Lender control** | ❌ Lender has less control | ✔️ Lender decides who can borrow |
| **Trust** | ❌ Riskier for valuable items | ✔️ Better for tools and technical devices |
| **Request management** | ❌ No accept/reject process | ✔️ Clear accept/reject workflow |
## 04: How should tools and devices be categorized?

### Meta

Status
: Decided

Updated
: 05-Jul-2025

### Problem statement

Users need an easy way to find tools and technical devices.

Without categories, searching becomes difficult when many items are listed.

### Decision

We decided to use categories.

Items can be grouped into categories such as tools, technical devices and others.

Decision was taken by: Maryam

### Regarded options

+ No categories
+ Categories
+ Tags

| Criterion | No categories | Categories | Tags |
| --- | --- | --- | --- |
| Easy to find items | ❌ | ✔️ | ✔️ |
| Simple implementation | ✔️ | ✔️ | ❌ |
| User friendly | ❌ | ✔️ | ✔️ |
## 05: How should API responses be formatted?

### Meta

Status
: Decided

Updated
: 05-Jul-2025

### Problem statement

The frontend needs a consistent way to receive data from the backend.

### Decision

We decided to return data as JSON objects.

JSON is easy to process in web applications and works well with APIs.

Decision was taken by: Maryam

### Regarded options

+ Plain text
+ JSON
+ XML

| Criterion | Plain Text | JSON | XML |
| --- | --- | --- | --- |
| Easy to use | ❌ | ✔️ | ❌ |
| Common for APIs | ❌ | ✔️ | ❌ |
| Readable | ✔️ | ✔️ | ❌ |