from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Create a SQLAlchemy object

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(150), nullable=False, unique=True)  # Username field
    email = db.Column(db.String(150), nullable=False, unique=True)  # Email field

    def __repr__(self):
        return f'<User {self.username}>'

"""
db = SQLAlchemy() # Create a new sqlalchemy object to manage our database 

class User(db.Model): defines a new model(or table)named 'user'
db.comlumn(...): defines the colums (or fields) in the table ...so each user has an id , username and email 
"""