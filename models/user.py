from db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    is_admin = db.Column(db.Boolean)

    def __init__(self, username: str, password: str, is_admin: bool) -> None:
        self.username = username
        self.password = password
        self.is_admin = is_admin