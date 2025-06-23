#This file creates Flask app and registers blueprints#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#Creates a data-base in SQLite:
db = SQLAlchemy()
DB_NAME = "database"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Bobejnrfaejnfe aejknf"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}.db"
    db.init_app(app)

    from .routes import core
    app.register_blueprint(core)
        #OR:
    #app.register_blueprint(core, url_prefix = "/")
    
    from .routes import auth
    app.register_blueprint(auth)

    from .models import User, Note
    create_database(app)

    #Something to do with logging in#
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    #-End-#

    return app


def create_database(app):
    if not path.exists('website/'+DB_NAME):
            app.app_context().push()
            db.create_all()
            print("Created new DataBase!")


#Note: Adding a Url prefix just means we dont have to add a / for the first route or first page
    #routes manually, since its done here already. We dont have to do it, but its better