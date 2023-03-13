from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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

    # Importing database models
    from .models import User, Note

    create_database(app)

    # Managing login variables
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Using this function to load the user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # Finds primary key which is the integer version

    return app

# Check if database already exists, if not it will create it
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')