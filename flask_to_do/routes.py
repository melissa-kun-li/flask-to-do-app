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
    if request.method == 'POST':
        old = Task.query.filter_by(id = task_id).first()
        new_task = request.form['task']
        if len(new_task) == 0 or len(new_task) > 75:
            flash('Task should be between 1 and 75 characters')
            return render_template('update.html', task = old)
        match = Task.query.filter_by(task = new_task).first()
        if match == None:
            old.task = new_task
            db.session.commit()
            return redirect(url_for('todo')) 
        else:
            flash('Task not updated: task name is already used')
            return render_template('update.html', task = old)
    else:
        task = Task.query.filter_by(id = task_id).first()
        return render_template('update.html', task = task)

@app.route('/delete/', methods = ['GET', 'POST'])
def delete():
    return 'Deleting Task'

@app.route('/clear-all/', methods = ['GET', 'POST'])
# db.dropall()?
def clear_all():
    return 'Clearing all Tasks'