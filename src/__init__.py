from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://todolist:todolist@localhost/todolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)

db = SQLAlchemy(app)
db.init_app(app)
db.app = app
migrate = Migrate(app, db, render_as_batch=True)
