from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!!!</h1>'

@app.route('/user/<username>')
def user(username):
    return 'Hello, User %s' % username

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Check out my latest %d post' % post_id