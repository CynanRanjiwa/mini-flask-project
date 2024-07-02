import os

class Config:
    SECRET_KEY = os.urandom(24)  # Secret key for session management
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/mydatabase'  # Database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications (not needed)


"""
SECRET_KEY = os.urandom(24) is like a special paasword for my app
SQLALCHEMY_DATABASE_URI : this is the connection string to our postgresql database...it tells sqlalchemy where to find our database and how to connect to it
SQLALCHEMY_TRACK_MODIFICATIONS : this setting disables tracking modifications of objects, which we dont need 
"""