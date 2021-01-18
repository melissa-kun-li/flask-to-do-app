from flask import render_template, url_for, request, flash, redirect
from flask_to_do import app, db, models
from flask_to_do.models import Task, User
from flask_to_do.forms import RegisterForm, LoginForm
from flask_login import login_user, current_user, logout_user
from sqlalchemy.exc import ArgumentError

@app.route('/', methods = ['GET', 'POST'])
def todo():
    if request.method == 'POST':
        if current_user.is_authenticated:
            task = request.form['task']
            if len(task) == 0 or len(task) > 75:
                flash('Task not added: task should be between 1 and 75 characters')
                return redirect(url_for('todo'))
            entry = Task.query.filter_by(task = task, user_id = current_user.id).first()
            if entry == None:
                new_task = Task(task = task, user_id = current_user.id)
                db.session.add(new_task)
                db.session.commit()
                return redirect(url_for('todo')) 
            else:
                flash('Task not added: task name is already used')
                return redirect(url_for('todo'))
        else:
            flash('Please register or signup for an account to get your own To Do List!')
            return redirect(url_for('todo'))
    else:
        if current_user.is_authenticated:
            tasks = current_user.tasks
        else:
            tasks = []
        return render_template('todo.html', tasks = tasks)

@app.route('/update/<task_id>', methods = ['GET', 'POST'])
def update(task_id):
    if request.method == 'POST':
        old = Task.query.filter_by(id = task_id).first()
        new_task = request.form['task']
        if len(new_task) == 0 or len(new_task) > 75:
            flash('Task should be between 1 and 75 characters')
            return render_template('update.html', task = old)
        entry = Task.query.filter_by(task = new_task, user_id = current_user.id).first()
        if entry == None:
            old.task = new_task
            db.session.commit()
            return redirect(url_for('todo')) 
        else:
            flash('Task not updated: task name is already used')
            return render_template('update.html', task = old)
    else: 
        if current_user.is_authenticated:
            task = Task.query.filter_by(id = task_id, user_id = current_user.id).first()
            if task == None:
                return redirect(url_for('todo'))
                # future: page not found
            return render_template('update.html', task = task)
        else:
            return redirect(url_for('todo'))
            # future: page not found

@app.route('/delete/<task_id>', methods = ['POST'])
def delete(task_id):
    task = Task.query.filter_by(id = task_id, user_id = current_user.id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo'))

@app.route('/clear-all/', methods = ['POST'])
def clear_all():
    if current_user.is_authenticated:
    # delete all tasks with user_id = current_user.id
        Task.query.filter_by(user_id = current_user.id).delete()
        db.session.commit() 
    else:
        flash('Please register or signup for an account to get your own To Do List!')
        return redirect(url_for('todo'))
    return redirect(url_for('todo'))

# make username case insensitive? 
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    # if user is already logged in:
    if current_user.is_authenticated:
        return redirect(url_for('todo'))
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user == None: 
            user = User(name = form.name.data, username = form.username.data)
            # IMPORTANT: don't store original password; store hashed passwords
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            # saves cookie, prevents user from being logged out when they close their browser
            login_user(user, remember = True)
        else:
            # flash message in the register.html
            flash('Username already in use. Please enter a different username')
            return redirect(url_for('register'))
        return redirect(url_for('todo')) 
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('todo'))
    if form.validate_on_submit:
        if request.method == 'POST': 
            user = User.query.filter_by(username = form.username.data).first()
            if user and user.validate_password(form.password.data):
                login_user(user, remember = True)
                next_page = request.args.get('next')
                # if next_page == None, redirect to home page
                return redirect(next_page) if next_page else redirect(url_for('todo'))
            else:
                flash("Username and password didn't match our records. Please try again")
                return redirect(url_for('login'))
    return render_template('login.html', form = form)

@app.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('todo'))

# @app.route('/settings', methods)