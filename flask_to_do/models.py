from flask_to_do import db

# future: make User class
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(75), unique = True) # nullable = False