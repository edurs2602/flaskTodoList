from flask import Flask, render_template, url_for, redirect, request

from src import db, app, login_manager
from src.models import User, Todo


@app.route("/")
def index():
    todo_lista = Todo.query.all()
    return render_template('index.html', todo_list=todo_lista)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.request_loader
def load_user_from_request(request):
    user = User.query.filter_by(username=request.form.get('username')).first()
    return user

@app.route("/add", methods=['POST'])
def add():
    task = request.form.get('task')
    newToDo = Todo(
        task=task,
        complete=False
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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("DB Created")
    app.run(debug=True)
