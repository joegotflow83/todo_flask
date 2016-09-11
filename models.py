from flask_sqlalchemy import SQLAlchemy

from config import DATABASE_PATH
from app import app


app.config['DATABASE_URI'] = DATABASE_PATH
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __str__(self):
        return "Email {}".format(self.email)
