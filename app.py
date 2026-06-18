from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/browse")
def browse():
    return render_template("browse.html")


@app.route("/create-item")
def create_item():
    return render_template("create_item.html")


@app.route("/requests")
def requests():
    return render_template("requests.html")


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


if __name__ == "__main__":
    app.run(debug=True)