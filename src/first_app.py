from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():
    return request.args.get('name','')

@app.route('/user/<username>')
def show_user_profile(username):
    return username

if __name__ == '__main__':
    app.run()
