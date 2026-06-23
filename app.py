from flask import Flask, render_template, jsonify

app = Flask(__name__)

# --- BESTEHENDE ROUTEN ---

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/items")
def api_items():
    items = [
        {"id": 1, "name": "Bohrmaschine", "status": "available"},
        {"id": 2, "name": "Leiter", "status": "available"}
    ]
    return jsonify(items)

# --- NEUE ROUTEN FÜR DIE TEMPLATES ---

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/browse")
def browse():
    # Temporäre leere Liste, um Fehler in der Jinja-Schleife zu vermeiden
    return render_template("items.html", items=[])

@app.route("/add_item")
def add_item():
    return render_template("add_item.html")

@app.route("/profile")
def profile():
    # Temporärer Dummy-Benutzer für das Profil-Template
    fake_user = {"first_name": "Yves", "last_name": "Nkwane", "email": "yves@beispiel.de"}
    return render_template("profile.html", user=fake_user, items=[])

@app.route("/item/<int:item_id>")
def item_detail(item_id):
    # Temporäres Dummy-Objekt für das Template
    fake_item = {
        "id": item_id,
        "name": "Bohrmaschine",
        "category": "Werkzeuge",
        "condition": "Gut",
        "description": "Eine hochwertige Bosch Schlagbohrmaschine, ideal für Heimwerkerprojekte.",
        "status": "available"
    }
    fake_owner = {"first_name": "Max", "last_name": "Mustermann"}
    return render_template("item_detail.html", item=fake_item, owner=fake_owner)

@app.route("/requests")
def requests_page():
    # Temporäre Dummy-Anfragen für das Template
    fake_requests = [
        {"id": 1, "item": "Bohrmaschine", "borrower": "Anna Schmidt", "status": "pending"},
        {"id": 2, "item": "Leiter", "borrower": "Tom Weber", "status": "accepted"}
    ]
    return render_template("requests.html", requests=fake_requests)

@app.route("/requests/<int:request_id>/accept")
def accept_request(request_id):
    # TODO: Alice muss hier die echte Logik implementieren
    return "Anfrage akzeptiert! (Platzhalter)"

@app.route("/requests/<int:request_id>/reject")
def reject_request(request_id):
    # TODO: Alice muss hier die echte Logik implementieren
    return "Anfrage abgelehnt! (Platzhalter)"

if __name__ == "__main__":
    app.run(debug=True)
