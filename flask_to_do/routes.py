from flask import render_template, url_for, request, flash, redirect
from flask_to_do import app, db, models
from flask_to_do.models import Task

@app.route('/', methods = ['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if len(task) == 0 or len(task) > 75:
            flash('Task should be between 1 and 75 characters')
            return redirect(url_for('todo'))
        new_task = Task(task = task)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('todo')) 
    else:
        tasks = Task.query.all() 
        return render_template('todo.html', tasks = tasks)

@app.route('/update/<task_id>', methods = ['GET', 'POST'])
def update(task_id):
    if request.method == 'POST':
        old = Task.query.filter_by(id = task_id).first()
        new_task = request.form['task']
        if len(new_task) == 0 or len(new_task) > 75:
            flash('Task should be between 1 and 75 characters')
            return render_template('update.html', task = old)
        old.task = new_task
        db.session.commit()
        return redirect(url_for('todo')) 
    else:
        task = Task.query.filter_by(id = task_id).first()
        db.session.commit()
        return render_template('update.html', task = task)

@app.route('/delete/<task_id>', methods = ['GET', 'POST'])
def delete(task_id):
    if request.method == 'POST':
        task = Task.query.filter_by(id = task_id).first()
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('todo'))
    else:
        tasks = Task.query.all() 
        return render_template('todo.html', tasks = tasks)

@app.route('/clear-all/', methods = ['GET', 'POST'])
def clear_all():
    if request.method == 'POST':
        models.Task.query.delete()
        db.session.commit() # need to commit
        return redirect(url_for('todo'))
    else:
        tasks = Task.query.all() 
        return render_template('todo.html', tasks = tasks)