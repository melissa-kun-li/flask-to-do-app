from flask import Flask, render_template, url_for, flash, request
# create instance of Flask class
app = Flask(__name__)

# set secret key to random bytes
app.config['SECRET_KEY'] = 'ffc47654e084968728400edc57de4531' # import secrets, secrets.token_hex(16)

# route() decorator tells Flask what URL to trigger function
@app.route('/', methods = ['GET', 'POST'])
def todo():
    return render_template('todo.html')

@app.route('/add-task/', methods = ['GET', 'POST']) # do i even need this route, can I just use the home route?
def add():
    # validate the task inputted? if it's less than 1 then flash an error? else: database
    return 'Adding task'

@app.route('/update-task/', methods = ['GET', 'POST'])
def update():
    return 'Updating Task'

@app.route('/delete-task/', methods = ['GET', 'POST'])
def delete():
    return 'Deleting Task'

@app.route('/clear-all-tasks/', methods = ['GET', 'POST'])
def clear_all():
    return 'Clearing all Tasks'
    
if __name__ == '__main__':
    # run app in Debug mode so don't have to restart manually after each change to code
    app.run(debug=True)

# cmd + shift + r to hard reload and empty cache