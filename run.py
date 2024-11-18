from flask import Flask
from app.controllers.book_controller import book_blueprint
from app.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(book_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

