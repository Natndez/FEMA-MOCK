from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abc123'
    # Configuring database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initializing database with Flask app
    db.init_app(app)

    # Must import our various views in our init file
    from .views import views
    from .auth import auth

    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')

    return app