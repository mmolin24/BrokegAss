from . import app
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
def hello_world():
    print("sarfas")
    return render_template('index.html', title="HomePage")


@app.route('/about')
def about():
    return 'Welcome to the world n'

@app.route('/user/<username>')
def profile(username):
    return 'this gas user is {}'.format(username)

@app.route('/feed')
def feed():
    return ''
    