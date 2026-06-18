from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

items = [
    {
        "id": 1,
        "title": "Bohrmaschine",
        "category": "Werkzeug",
        "description": "Für kleine Reparaturen und Umzüge",
        "status": "available"
    },
    {
        "id": 2,
        "title": "Beamer",
        "category": "Technik",
        "description": "Für Präsentationen oder Filmabende.",
        "status": "available"
    }
]

requests = [
    {
        "id": 1,
        "item": "Bohrmaschine",
        "borrower": "Jean",
        "status": "pending"
    },
    {
        "id": 2,
        "item": "Beamer",
        "borrower": "Maryam",
        "status": "accepted"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/browse")
def browse():
    return render_template("browse.html", items=items)


@app.route("/item/<int:item_id>")
def item_detail(item_id):
    selected_item = None

    for item in items:
        if item["id"] == item_id:
            selected_item = item

    return render_template("item_detail.html", item=selected_item)


@app.route("/create-item", methods=["GET", "POST"])
def create_item():
    if request.method == "POST":
        new_item = {
            "id": len(items) + 1,
            "title": request.form["title"],
            "category": request.form["category"],
            "description": request.form["description"],
            "status": "available"
        }

        items.append(new_item)
        return redirect(url_for("browse"))

    return render_template("create_item.html")

@app.route("/requests")
def requests_page():
    return render_template("requests.html", requests=requests)


@app.route("/requests/<int:request_id>/accept")
def accept_request(request_id):
    for request_item in requests:
        if request_item["id"] == request_id:
            request_item["status"] = "accepted"

    return redirect(url_for("requests_page"))


@app.route("/requests/<int:request_id>/reject")
def reject_request(request_id):
    for request_item in requests:
        if request_item["id"] == request_id:
            request_item["status"] = "rejected"

    return redirect(url_for("requests_page"))


@app.route("/api/items")
def api_items():
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)