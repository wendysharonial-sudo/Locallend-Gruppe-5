from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from database.models import db, User

app = Flask(__name__)

app.secret_key = "locallend-security-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///locallend.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

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

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        first_name = request.form["first_name"]

        last_name = request.form["last_name"]

        email = request.form["email"]

        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            return "Email already registered."

        hashed_password = generate_password_hash(password)

        new_user = User(

            first_name=first_name,

            last_name=last_name,

            email=email,

            password=hashed_password

        )

        db.session.add(new_user)

        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])

def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.user_id

            session["user_name"] = user.first_name

            return redirect(url_for("home"))

        return "Login failed."

    return render_template("login.html")

@app.route("/logout")

def logout():

    session.clear()

    return redirect(url_for("home"))


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