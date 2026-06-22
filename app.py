from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/items")
def api_items():
    items = [
        {
            "id": 1,
            "name": "Bohrmaschine",
            "category": "Werkzeug",
            "status": "available"
        },
        {
            "id": 2,
            "name": "Leiter",
            "category": "Werkzeug",
            "status": "available"
        }
    ]

    return jsonify({
        "success": True,
        "message": "Items loaded successfully",
        "data": items
    })


@app.route("/api/requests")
def api_requests():
    requests = [
        {
            "id": 1,
            "item": "Bohrmaschine",
            "borrower": "Max",
            "status": "pending"
        },
        {
            "id": 2,
            "item": "Leiter",
            "borrower": "Anna",
            "status": "accepted"
        },
        {
            "id": 3,
            "item": "Beamer",
            "borrower": "Sara",
            "status": "rejected"
        }
    ]

    return jsonify({
        "success": True,
        "message": "Requests loaded successfully",
        "data": requests
    })


@app.route("/api/create_request")
def create_request():
    new_request = {
        "id": 4,
        "item": "Laptop",
        "borrower": "Maryam",
        "status": "pending"
    }

    return jsonify({
        "success": True,
        "message": "Request created successfully",
        "data": new_request
    })


@app.route("/api/accept_request")
def accept_request():
    request = {
        "id": 1,
        "status": "accepted"
    }

    return jsonify({
        "success": True,
        "message": "Request accepted successfully",
        "data": request
    })


@app.route("/api/reject_request")
def reject_request():
    request = {
        "id": 2,
        "status": "rejected"
    }

    return jsonify({
        "success": True,
        "message": "Request rejected successfully",
        "data": request
    })


@app.route("/api/delete_request")
def delete_request():
    request = {
        "id": 3,
        "status": "deleted"
    }

    return jsonify({
        "success": True,
        "message": "Request deleted successfully",
        "data": request
    })


@app.route("/api/status")
def api_status():
    status = {
        "api": "LocalLend API",
        "version": "1.0",
        "status": "running",
        "available_endpoints": [
            "/api/items",
            "/api/requests",
            "/api/create_request",
            "/api/accept_request",
            "/api/reject_request",
            "/api/delete_request",
            "/api/status"
        ]
    }

    return jsonify({
        "success": True,
        "message": "API is running",
        "data": status
    })


if __name__ == "__main__":
    app.run(debug=True)g