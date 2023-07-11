from flask import Flask, render_template, url_for, redirect, request

from src import db, app
from src.models import Todo

@app.route("/todo")
def index():
    todo_lista = Todo.query.all()
    return render_template('todo.html', todo_list=todo_lista)

@app.route("/add", methods=['POST'])
def add():
    task = request.form.get('task')
    newToDo = Todo(
        task=task,
        complete=False
    )
    db.session.add(newToDo)
    db.session.commit()
    return redirect('/todo')


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todoId = Todo.query.filter_by(id=todo_id).update(dict(complete=True))
    db.session.commit()
    return redirect('/todo')


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todoId = Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()
    return redirect('/todo')

