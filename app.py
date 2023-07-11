from src import db, app
from src import todo, user

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("DB Created")
    app.run(debug=True)
