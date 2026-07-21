from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "users"

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    items = db.relationship("Item", backref="owner", lazy=True)
    requests = db.relationship("Request", backref="borrower", lazy=True)



class Item(db.Model):
    __tablename__= "items"

    item_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description= db.Column(db.Text)
    category = db.Column(db.String(100))
    availability = db.Column(db.String(50), default="available")
   


class Request(db.Model):
    __tablename__ = "requests"

    request_id = db.Column(db.Integer, primary_key=True)
    item_id= db.Column(db.Integer, db.ForeignKey("items.item_id"), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    status = db.Column(db.String(50), default="pending")
  