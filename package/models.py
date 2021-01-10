from package import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    fname = db.Column(db.String(20), unique=False, nullable=False)
    lname = db.Column(db.String(20), unique=False, nullable=False)
    image_user = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    items = db.relationship('Item', backref='seller', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_user}')"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(25), nullable=False)
    item_stock = db.Column(db.Integer, nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    item_image = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Item('{self.name}', '{self.description}', '{self.price}', '{self.item_image}')"

class Trasaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyers_name = db.Column(db.String(20), nullable=False)
    item_name = db.Column(db.String(350), nullable=False)
    stock_buy = db.Column(db.Integer, nullable=False)
    total_ammount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80))

    def __repr__(self):
        return f"Trasaction('{self.buyers_name}', '{self.item_name}', '{self.stock_buy}', '{self.total_ammount}', '{self.description}')"
