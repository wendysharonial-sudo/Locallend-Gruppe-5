Design Decisions

01: Provide item and request data through a JSON API

Meta

Status
: Decided

Updated
: 23-Jun-2026

Team
: LocalLend

Lead
: Maryam

Problem statement

LocalLend is a Flask web application for borrowing and lending tools and technical devices.

Users need access to item data and lending request data. The project also requires at least one headless API endpoint that returns data as JSON.

Therefore, we had to decide whether this data should only be shown on HTML pages or also be provided through a structured JSON API.

Decision

We decided to provide selected item and request data through a JSON API.

JSON is structured, machine-readable and independent from the HTML layout. This makes the data easier to test, document and reuse. It also fulfils the project requirement of providing at least one headless API endpoint.

Decision was taken by: Maryam

Regarded options

We regarded two options:

* Show data only through HTML pages.
* Provide selected data through a JSON API.

Criterion	HTML pages only	JSON API
Human users	Easy to read in the browser	Not designed as a visual page
Structured data	Data is mixed with HTML	Data is clearly structured
Project requirement	Does not fulfil the JSON API requirement	Fulfils the JSON API requirement
Testing	Harder to test separately	Easy to test through API endpoints
Documentation	Harder to document as an interface	Endpoints and responses can be documented clearly

⸻

02: Manage lending requests through status values

Meta

Status
: Decided

Updated
: 23-Jun-2026

Team
: LocalLend

Lead
: Maryam

Problem statement

Borrowers can send lending requests for tools and technical devices.

A request does not end immediately after it is created. First, it is open. Then the lender can either accept or reject it. The application therefore needs a clear way to represent the current state of each request.

We had to decide whether handled requests should disappear after a decision or whether they should remain visible with a status value.

Decision

We decided to keep lending requests in the system and manage them through status values.

A new request starts with the status pending. If the lender accepts the request, the status changes to accepted. If the lender rejects the request, the status changes to rejected.

This makes the request process easier to understand, explain and debug.

Decision was taken by: Maryam

Regarded options

We regarded two options:

* Delete requests after they are handled.
* Keep requests and update their status.

Criterion	Delete handled requests	Store request status
Simplicity	Less data remains visible	Requires an additional status value
Traceability	Hard to see what happened later	Request history remains understandable
User understanding	Request may suddenly disappear	User can see pending, accepted or rejected
Request workflow	No clear lifecycle	Clear lifecycle from pending to accepted/rejected
Debugging	Harder to check previous states	Easier to inspect the current state

⸻

03: Use request-based lending instead of automatic lending

Meta

Status
: Decided

Updated
: 23-Jun-2026

Team
: LocalLend

Lead
: Maryam

Problem statement

LocalLend focuses on tools and technical devices. These items can be valuable, fragile or personally important to the lender.

We had to decide whether borrowers should be able to borrow an item automatically or whether the lender should first approve each request.

This decision is important because lenders should keep control over who borrows their tools or technical devices.

Decision

We decided to use request-based lending.

Borrowers can send a lending request, but the item is not automatically borrowed. The lender must accept or reject the request.

This gives lenders more control and fits the focus on tools and technical devices, because these items often require trust and careful handling.

Decision was taken by: Maryam

Regarded options

We regarded two options:

* Automatic lending after a borrower selects an item.
* Request-based lending with lender approval.

Criterion	Automatic lending	Request-based lending
Speed	Faster for borrowers	Borrower must wait for approval
Lender control	Lender has less control	Lender decides who can borrow
Trust	Riskier for valuable items	Better for tools and technical devices
Request management	No accept/reject process	Clear accept/reject workflow
Fit for LocalLend	Too automatic for personal items	Fits local lending between people

⸻

04: Categorize tools and technical devices

Meta

Status
: Decided

Updated
: 23-Jun-2026

Team
: LocalLend

Lead
: Maryam

Problem statement

Users need an easy way to find tools and technical devices.

Without categories, searching becomes difficult when many items are listed. This is especially relevant for LocalLend because tools and technical devices can belong to different groups, such as power tools, electronic devices or accessories.

We had to decide whether items should be listed without structure, grouped into fixed categories or described with flexible tags.

Decision

We decided to use fixed categories for listed items.

Items can be grouped into categories such as tools, technical devices and others. This makes it easier for borrowers to find relevant items and gives lenders a clearer structure when adding an item.

Fixed categories are simple enough for the current prototype and can later be extended if needed.

Decision was taken by: Maryam

Regarded options

We regarded three options:

* No categories.
* Fixed categories.
* Flexible tags.

Criterion	No categories	Fixed categories	Flexible tags
Easy to find items	Harder when many items exist	Clear structure	Useful for detailed search
Simple implementation	Very simple	Manageable	More complex
User friendliness	Less guidance for users	Easy to understand	Can become inconsistent
Fit for tools/devices	Too unstructured	Good fit	Good, but more effort
Future extension	Limited	Can be extended later	Flexible from the start

⸻

05: Format API responses as JSON objects

Meta

Status
: Decided

Updated
: 23-Jun-2026

Team
: LocalLend

Lead
: Maryam

Problem statement

The frontend, documentation and testing process need a consistent way to understand data returned by the backend.

Because the project includes a JSON API, we had to decide how API responses should be formatted. The response format should be easy to read, easy to document and suitable for structured item and request data.

Decision

We decided to return API responses as JSON objects or lists of JSON objects.

JSON is easy to inspect, common for web APIs and works well with Flask through jsonify. This makes the API easier to test and explain.

For single actions, such as accepting or rejecting a request, the API returns one JSON object. For lists, such as all items or all requests, the API returns a list of JSON objects.

Decision was taken by: Maryam

Regarded options

We regarded three options:

* Plain text.
* JSON.
* XML.

Criterion	Plain text	JSON	XML
Easy to inspect	Simple text	Readable structure	More verbose
Common for APIs	Not suitable for structured APIs	Very common	Possible, but less common in this context
Structured data	Hard to represent item/request fields	Good for objects and lists	Structured, but more complex
Fit with Flask	Manual formatting needed	Works well with jsonify	More effort
Documentation	Harder to document consistently	Easy to document with examples	More complex to explain

⸻