from flask import Flask, render_template
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config class

db.init_app(app)  # Initialize the database with the Flask app

@app.route('/')
def index():
    users = User.query.all()  # Get all users from the database
    return render_template('index.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create all database tables
    app.run(debug=True)  # Run the Flask app


"""
app = Flask(__name__): Creates a new Flask application.

app.config.from_object(Config): Loads configuration settings from the Config class.

db.init_app(app): Initializes the SQLAlchemy database with our Flask app.

@app.route('/'): Defines a route for the home page. When someone visits the root URL, this function is called.

users = User.query.all(): Queries the database to get all users.

render_template('index.html', users=users): Renders the index.html template and passes the list of users to it.

if __name__ == '__main__':: This ensures that the Flask app runs only if this file is executed directly.

db.create_all(): Creates all the database tables defined in models.py.

"""