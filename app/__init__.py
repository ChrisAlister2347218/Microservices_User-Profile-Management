from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/user_profiles'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Import and register parts of our application
        from . import routes
        app.register_blueprint(routes.bp)  # Register the blueprint

        # Create tables if they don't exist
        db.create_all()

    return app
