# :ballot_box_with_check: To Do App

Hosted at: https://mel-to-do.herokuapp.com 

This to do list web app is built using Flask, PostgresSQL, and Bootstrap. I built this to extend my simple command line to do program, and to learn SQL and full-stack development!

## Features:
1. Each user has a private and unique to do list after user registration and login with authentication
2. Add a new task to the to do list (checks for duplicate)
3. View all tasks
4. Update/edit a task (checks for duplicate)
5. Delete a task 
6. Clear all tasks 

## Some things I learned after I completed this project:
- how to run a Linux server on a virtual machine (for testing I ran a Postgres database in CentOS; while the web app uses the Heroku Postgres service) 
- how to set up a MySQL and Postgres database 
- how to use SQL
- how to implement a one-to-many relationship in Flask-SQLAlchemy
- HTML and CSS
- how to customize Bootstrap
- how to handle GET and POST requests
- using Flask-SQLAlchemy to easily switch between databases (went from SQlite -> MySQL -> Postgres)
- validating user input and handling forms with Flask-WTF
- password hashing
- how to set environment variables to store credentials
- how to deploy an app with Heroku
