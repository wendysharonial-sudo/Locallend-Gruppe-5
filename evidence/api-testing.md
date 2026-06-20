API Testing Documentation

Responsible

Maryam – API & Request System

Purpose

The API endpoints were tested locally to verify that they return valid JSON responses and behave as expected.

⸻

Tested Endpoints

/api/items

Method: GET

Expected Result:

Returns all available items as JSON.

Status: Passed

⸻

/api/requests

Method: GET

Expected Result:

Returns all lending requests and their current status.

Status: Passed

⸻

/api/create_request

Method: GET

Expected Result:

Creates a new lending request with the status pending.

Status: Passed

⸻

/api/accept_request

Method: GET

Expected Result:

Changes the request status to accepted.

Status: Passed

⸻

/api/reject_request

Method: GET

Expected Result:

Changes the request status to rejected.

Status: Passed

⸻

/api/delete_request

Method: GET

Expected Result:

Changes the request status to deleted.

Status: Passed

⸻

/api/status

Method: GET

Expected Result:

Returns information about the API and all available endpoints.

Status: Passed

⸻

Test Results

All API endpoints returned valid JSON responses.

The response structure was consistent across all endpoints and included:

* success
* message
* data

The status values pending, accepted, rejected, deleted, and available were returned correctly.

⸻

Technologies Used

* Python
* Flask
* JSON
* Browser Testing
* Git
* GitHub

⸻

Conclusion

The API was successfully tested and all implemented endpoints behaved as expected. The request workflow and status management were verified through manual testing in the browser.

