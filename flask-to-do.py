from flask import Flask, render_template, url_for, request, flash
# create instance of Flask class
app = Flask(__name__)

# set secret key to random bytes
app.config['SECRET_KEY'] = 'ffc47654e084968728400edc57de4531' # import secrets, secrets.token_hex(16)

# route() decorator tells Flask what URL to trigger function
@app.route('/', methods = ['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if len(task) == 0 or len(task) > 75:
            flash('Task should be between 1 and 75 characters')
    # query the database, show all the tasks still
    return render_template('todo.html')

# head and alert should be part of a base.html because everything will need it, take out of todo.html
# need an edit html

# use id of the task in the url from the database? or how will it know what to update and what to delete?
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