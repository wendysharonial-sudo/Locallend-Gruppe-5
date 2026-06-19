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
            "status": "available"
        },
        {
            "id": 2,
            "name": "Leiter",
            "status": "available"
        }
    ]

    return jsonify(items)


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

    return jsonify(requests)


@app.route("/api/create_request")
def create_request():

    new_request = {
        "id": 4,
        "item": "Laptop",
        "borrower": "Maryam",
        "status": "pending"
    }

    return jsonify(new_request)


@app.route("/api/accept_request")
def accept_request():

    request = {
        "id": 1,
        "status": "accepted"
    }

    return jsonify(request)


@app.route("/api/reject_request")
def reject_request():

    request = {
        "id": 2,
        "status": "rejected"
    }

    return jsonify(request)


@app.route("/api/delete_request")
def delete_request():

    request = {
        "id": 3,
        "status": "deleted"
    }

    return jsonify(request)


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
            "/api/delete_request"
        ]
    }

    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=True)