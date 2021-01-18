from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# import pymysql
import psycopg2
import os
import sqlite3

# NEED TO CHANGE FROM CLEARDB TO SOMETHING ELSE
app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'test')

app.config['SECRET_KEY'] = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_TODO', 'sqlite:///todo.db')
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 60} # clearDB keep connection alive
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask_to_do import routes