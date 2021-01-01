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
def test():
    # validate the task inputted? if it's less than 1 then flash an error? else: database
    return 'Hi'

if __name__ == '__main__':
    # run app in Debug mode so don't have to restart manually after each change to code
    app.run(debug=True)

# cmd + shift + r to hard reload and empty cache