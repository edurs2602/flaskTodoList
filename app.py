from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.app = app


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(128))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_lista = Todo.query.all()
    return render_template('index.html', todo_list=todo_lista)


@app.route("/add", methods=['POST'])
def add():
    task = request.form.get('task')
    newToDo = Todo(
        task = task,
        complete = False
    )
    db.session.add(newToDo)
    db.session.commit()
    return redirect('/')


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todoId = Todo.query.filter_by(id=todo_id).update(dict(complete=True))
    db.session.commit()
    return redirect('/')


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todoId = Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()
    return redirect('/')


if __name__=='__main__':
    db.create_all()
    app.run(debug=False, port=int("5000"))