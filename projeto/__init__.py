import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#CREATE A LOGIN MANAGER OBJECT
login_manager = LoginManager()

#CREATE MY APPLICATION
app = Flask(__name__)

# CREATE MY DATABASE
app.config['SECRET_KEY'] = 'secret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#CONFIGURATE MY DATABASE WITH THE APP STRUCTURE
db = SQLAlchemy(app)
Migrate(app,db)

#Pass in our app to the login MANAGER
login_manager.init_app(app)

# Tell users what view to go when they need to login_manager
login_manager.login_view = 'login'
