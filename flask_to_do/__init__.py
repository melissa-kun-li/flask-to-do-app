from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import pymysql
import psycopg2
import os

# NEED TO CHANGE FROM CLEARDB TO SOMETHING ELSE
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'test')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_TODO')
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 60} # clearDB keep connection alive
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask_to_do import routes