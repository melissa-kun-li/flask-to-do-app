from flask import render_template, url_for, request, flash
from flask_to_do import app
from flask_to_do.models import Task

# route() decorator tells Flask what URL to trigger function
@app.route('/', methods = ['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if len(task) == 0 or len(task) > 75:
            flash('Task should be between 1 and 75 characters')
    # else if request.method == 'GET':
        # query the database, show all the tasks still
        # return this stuff
    # database, then return redirect(url_for('update'), task_id = ?)
    return render_template('todo.html')

# need an edit.html

# use id of the task in the url from the database? 
@app.route('/update/<task_id>', methods = ['GET', 'POST'])
# <> pass to value as parameter
def update(task_id):
    return 'Updating Task'

@app.route('/delete/', methods = ['GET', 'POST'])
def delete():
    return 'Deleting Task'

@app.route('/clear-all/', methods = ['GET', 'POST'])
# db.dropall()?
def clear_all():
    return 'Clearing all Tasks'