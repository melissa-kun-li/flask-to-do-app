from flask import render_template, url_for, request, flash, redirect
from flask_to_do import app, db, models
from flask_to_do.models import Task, User
from flask_to_do.forms import RegisterForm, LoginForm
from flask_login import login_user, current_user

@app.route('/', methods = ['GET', 'POST'])
# check for task name uniqueness, flash error msg
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if len(task) == 0 or len(task) > 75:
            flash('Task not added: task should be between 1 and 75 characters')
            return redirect(url_for('todo'))
        new_task = Task(task = task)
        entry = Task.query.filter_by(task = task).first()
        if entry == None:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('todo')) 
        else:
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

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    # if user is already logged in:
    if current_user.is_authenticated:
        return redirect(url_for('todo'))
    if form.validate_on_submit():
        if request.method == 'POST':
            user = User.query.filter_by(username = form.username.data).first()
            if user == None: 
                user = User(name = form.name.data, username = form.username.data)
                # IMPORTANT: don't store original password; store hashed passwords!
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                # saves cookie, prevents user from being logged out when they chose their browser
                login_user(user, remember = True)
            else:
                # flash message in the register.html
                flash('Username already in use')
                return redirect(url_for('register'))
            return redirect(url_for('todo')) 
    else:
        return render_template('register.html', form = form)

# make login.html
@app.route('/login', methods = ['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form = form)