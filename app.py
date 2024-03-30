from flask import render_template, send_from_directory

from src import db, app
from src import todo, user


@app.route('/')
def home():
    return render_template('index.html')


# Serve React app
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('frontend/todolist/build/static', path)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('frontend/todolist/build', 'index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
