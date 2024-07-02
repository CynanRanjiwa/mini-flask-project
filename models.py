from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Create a SQLAlchemy object

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(150), nullable=False, unique=True)  # Username field
    email = db.Column(db.String(150), nullable=False, unique=True)  # Email field

    def __repr__(self):
        return f'<User {self.username}>'
