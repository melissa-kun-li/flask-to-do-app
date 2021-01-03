from flask_to_do import db
from flask_to_do import app

if __name__ == '__main__':
    db.create_all()
    # run app in Debug mode so don't have to restart manually after each change to code
    app.run(debug=True)

# cmd + shift + r to hard reload and empty cache