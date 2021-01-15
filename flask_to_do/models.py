from flask_to_do import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(75), unique = True) 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25))
    username = db.Column(db.String(25), unique = True)
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # returns True if password hash matches password user entered; else returns False
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)



