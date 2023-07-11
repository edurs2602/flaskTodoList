from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_user, logout_user

from src import db, app, login_manager
from src.models import User

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            pwd = request.form['password']

            newUser = User(username, email, pwd)
            db.session.add(newUser)
            db.session.commit()

            return redirect('/')
        

        return render_template('register.html')
    except:
        error = "User register error"
        context = {
            'error' : error
        }

        return render_template('error.html', **context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            pwd = request.form['password']

            user = User.query.filter_by(email=email).first()

            if not user or not user.check_password(pwd):
                return redirect('/')

            login_user(user)
            return redirect('/')

        return render_template('login.html')
    except:
        error = "User login error"
        context = {
            'error' : error
        }

        return render_template('error.html', **context)

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

@login_manager.request_loader
def load_user_from_request(request):
    user = User.query.filter_by(username=request.form.get('username')).first()
    return user

@app.route('/logout')
def logout():
    try:
        logout_user()
        return redirect(url_for('login'))
    except:
        error = "User logout error"
        context = {
            'error' : error
        }

        return render_template('error.html', **context)

