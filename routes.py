from . import app

@app.route('/')
@app.route('/index')
def hello_world():
    return '<h1>Hello World</h1>'


@app.route('/about')
def about():
    return 'Welcome to the world n'

@app.route('/user/<username>')
def profile(username):
    return 'this gas user is {}'.format(username)

@app.route('/feed')
def feed():
    return ''
    