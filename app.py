from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from database.models import db, User, Item, Request as BorrowRequest

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///locallend.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

    existing_user = db.session.execute(db.select(User)).first()
    
    if existing_user is None:
        user1 = User(
        first_name="Anna",
        last_name="Müller",
        email="anna@example.com",
        password="test123"

        )

        user2 = User(
        first_name="Max",
        last_name="Soleil",
        email="max@example.com",
        password="test123"


        )

        db.session.add_all([user1,user2])
        db.session.commit()

        item1 = Item(
        user_id= user1.user_id,
        title="Bohrmachine",
        category= "Werkzeug",
        description= "Für kleine Reperaturen und Umzüge",
        availability= "available"
        )

        item2 = Item(
        user_id= user2.user_id,
        title= "Beamer",
        category="Technik",
        description="Für Präsentationen oder Filmabende",
        availability="available"
        )

        db.session.add_all([item1, item2])
        db.session.commit()



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
    items = db.session.execute(db.select(Item)).scalars().all()
    return render_template("browse.html", items=items)


@app.route("/item/<int:item_id>")
def item_detail(item_id):
    selected_item = db.session.get(Item, item_id)

    if selected_item is None:
        abort(404)
   
    return render_template("item_detail.html", item=selected_item)


@app.route("/create-item", methods=["GET", "POST"])
def create_item():

    if request.method == "POST":
        new_item = Item(
            user_id=1,
            title=request.form["title"],
            category=request.form["category"],
            description=request.form["description"],
            availability="available"
        )

        db.session.add(new_item)
        db.session.commit()

        return redirect(url_for("browse"))

    return render_template("create_item.html")

@app.route("/requests")
def requests_page():
    requests = db.session.execute(db.select(BorrowRequest)).scalars().all
    return render_template("requests.html", requests=requests)


@app.route("/requests/<int:request_id>/accept")
def accept_request(request_id):
   
    request_item = db.session.get(BorrowRequest, request_id)

    if request_item is None:
        abort(404)

    request_item.status = "accepted"

    db.session.commit()

    return redirect(url_for("requests_page"))


@app.route("/requests/<int:request_id>/reject")
def reject_request(request_id):
    
    request_item = db.session.get(BorrowRequest, request_id)

    if request_item is None:
        abort(404)

    request_item.status = "rejected"

    db.session.commit()

    return redirect(url_for("requests_page"))


@app.route("/api/items")
def api_items():
    items = db.session.execute(db.select(Item)).scalars().all()

    items_data = []

    for item in items:
        items_data.append({
            "id": item.item_id,
            "title": item.title,
            "category": item.category,
            "description": item.description,
            "status": item.availability
        })

    return jsonify(items_data)

if __name__== "__main__":
    app.run(debug=True)