from flask import render_template

from src import db, app
from src import todo, user

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("DB Created")
    app.run(debug=True)
