from flask import render_template, url_for, request, flash, redirect
from flask_to_do import app, db, models
from flask_to_do.models import Task
from sqlalchemy import exc

@app.route('/', methods = ['GET', 'POST'])
# check for task name uniqueness, flash error msg
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if len(task) == 0 or len(task) > 75:
            flash('Task not added: task should be between 1 and 75 characters')
            return redirect(url_for('todo'))
        new_task = Task(task = task)
        db.session.add(new_task)
        try: 
            db.session.commit()
            return redirect(url_for('todo')) 
        except exc.IntegrityError:
            flash('Task not added: task name is already used')
            return redirect(url_for('todo'))
    else:
        tasks = Task.query.all() 
        return render_template('todo.html', tasks = tasks)

@app.route('/update/<task_id>', methods = ['GET', 'POST'])
# check for task name uniqueness, flash error msg
def update(task_id):
    if request.method == 'POST':
        old = Task.query.filter_by(id = task_id).first()
        new_task = request.form['task']
        if old.task == new_task:
            flash('Task not added: task name is already used')
            return render_template('update.html', task = old)
        if len(new_task) == 0 or len(new_task) > 75:
            flash('Task should be between 1 and 75 characters')
            return render_template('update.html', task = old)
        old.task = new_task
        try:
            db.session.commit()
            return redirect(url_for('todo')) 
        except exc.IntegrityError:
            db.session.rollback()
            flash('Task not added: task name is already used')
            return render_template('update.html', task = old)
    else:
        task = Task.query.filter_by(id = task_id).first()
        return render_template('update.html', task = task)

@app.route('/delete/<task_id>', methods = ['POST'])
def delete(task_id):
    task = Task.query.filter_by(id = task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo'))

@app.route('/clear-all/', methods = ['POST'])
def clear_all():
    models.Task.query.delete()
    db.session.commit() # need to commit
    return redirect(url_for('todo'))
