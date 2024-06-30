from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 

db = SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqldb://23_webapp_00:TDaCk9Aj@mysql.lab.it.uc3m.es/23_webapp_00a"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Register blue prints
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
