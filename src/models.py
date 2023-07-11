from flask_bcrypt import bcrypt
from . import db, app, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, pwd):
        return bcrypt.check_password_hash(self.password, pwd)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(128))
    complete = db.Column(db.Boolean)
    