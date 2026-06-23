from flask import Flask, render_template, request, redirect, url_for, jsonify, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
from database.models import db, User, Item, Request as BorrowRequest

app = Flask(__name__)

app.secret_key = "locallend-security-key"
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
        password=generate_password_hash("test123")

        )

        user2 = User(
        first_name="Max",
        last_name="Soleil",
        email="max@example.com",
        password=generate_password_hash("test123")

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
        
        existing_user = db.session.execute(
            db.select(User).filter_by(email=email)
        ).scalar()

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

        user = db.session.execute(
            db.select(User).filter_by(email=email)
        ).scalar()

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

@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = db.session.get(User, session["user_id"])

    my_items = db.session.execute(
        db.select(Item).filter_by(user_id=session["user_id"])
    ).scalars().all()

    return render_template("profile.html", user=user, my_items=my_items)

@app.route("/items")
def items_page():
    database_items = db.session.execute(db.select(Item)).scalars().all()

    items = []
    for item in database_items:
        items.append({
            "name": item.title,
            "status": item.availability
        })

    return render_template("items.html", items=items)



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


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        name = request.form.get("name") or request.form.get("title")
        description = request.form["description"]
        category = request.form["category"]

        new_item = Item(
            user_id=session["user_id"],
            title=name,
            description=description,
            category=category,
            availability="available"
        )

        db.session.add(new_item)
        db.session.commit()

        return redirect(url_for("items_page"))

    return render_template("add_item.html")


@app.route("/requests")
def requests_page():
    database_requests = db.session.execute(db.select(BorrowRequest)).scalars().all()

    requests = []
    
    for request_item in database_requests:

        item = db.session.get(Item, request_item.item_id)
        borrower = db.session.get(User, request_item.borrower_id)

        requests.append({
            "id": request_item.request_id,
            "item": item.title if item else "Unknown item",
            "borrower": borrower.first_name if borrower else "Unknown user",
            "status": request_item.status
        })
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

@app.route("/api/requests")
def api_requests():
    database_requests = db.session.execute(db.select(BorrowRequest)).scalars().all()

    requests_data = []

    for requests_item in database_requests:
        item = db.session.get(Item, request_item.item_id)
        borrower = db.session.get(User,request_item.borrower_id)

        requests_data.append({

            "id": request_item.request_id,
            "item": item.title if item else "Unknown item",
            "borrower": borrower.first_name if borrower else "Unknown user",
            "status": request_item.status

        })

    return jsonify({

        "success": True,
        "message": "Requests loaded successfully",
        "data": requests_data

    })

@app.route("/api/status")
def api_status():

    return jsonify({

        "success": True,
        "message": "API is running",
        "data": {

            "api": "LocalLend API",
            "version": "1.0",
            "status": "running",
            "available_endpoints": [

                "/api/items",
                "/api/requests",
                "/api/status"

            ]

        }

    })


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__== "__main__":
    app.run(debug=True)