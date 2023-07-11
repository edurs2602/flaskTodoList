from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_user, logout_user

from src import db, app, login_manager
from src.models import User

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['password']

        newUser = User(username, email, pwd)
        db.session.add(newUser)
        db.session.commit()
    

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form['email']
    pwd = request.form['password']

    user = User.query.filter_by(email=email).first()

    if not user or user.check_password(pwd):
        return redirect('/')

        login_user(user)
        return redirect('/')

    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.request_loader
def load_user_from_request(request):
    user = User.query.filter_by(username=request.form.get('username')).first()
    return user

@app.route('/logout')
def logout():
    login_user()
    return redirect(url_for('/login'))

