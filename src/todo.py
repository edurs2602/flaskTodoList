from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_user, logout_user, current_user, login_required

from src import db, app, user
from src.models import Todo

@app.route("/todo")
@login_required
def index():
    todo_list = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('todo.html', todo_list=todo_list)

@app.route("/add", methods=['POST'])
@login_required
def add():
    task = request.form.get('task')
    error = None

    if task == "":
        error = "Task null error"
        context = {
            'error' : error
        }

        return render_template('error.html', **context)

    try:
        new_todo = Todo(
            task=task,
            complete=False,
            user_id=current_user.id
        )
        db.session.add(new_todo)
        db.session.commit()
    except:
        error = "Todo create error"
        context = {
            'error' : error
        }

        return render_template('error.html', **context)

    return redirect('/todo')

@app.route("/update/<int:todo_id>")
@login_required
def update(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo.user_id == current_user.id:
            todo.complete = True
            db.session.commit()
        return redirect('/todo')
    except:
        error = "Todo update error"
        context = {
            'error' : error
        }

        return render_template('error.html', **context)

@app.route("/delete/<int:todo_id>")
@login_required
def delete(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo.user_id == current_user.id:
            db.session.delete(todo)
            db.session.commit()
        return redirect('/todo')
    except:
        error = "Todo delete error"
        context = {
            'error' : error
        }

        return render_template('error.html', **context)

