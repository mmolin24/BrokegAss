<<<<<<< HEAD

=======
import json
import pyrebase
>>>>>>> 1391c4afe75eb941a086b5dd2e44cdc8e3a847b1
from flask import Flask, render_template, request, redirect, url_for
# from wtforms_fields import *
#from flask_monogoengine import MongoEngine
#from flask_wtf import FlaskForm
#from wtforms_fields import *
#from wtforms.validators import DataRequired
# ls check what's in the directory
# cd change to directory or do cd ~ to go to home directory
# mkdir makes a directory e.a.  mkdir hey       makes a directory named hey
# rm -filename removes the file, if you wanna delete a directory do rm -r -directory name
# pip install -library name


app = Flask(__name__)
<<<<<<< HEAD
#app.conif['SECRET_KEY']='downbadsquadgg'
 
=======
app.config["SECRET_KEY"] = "a"

config = {
    "apiKey": "AIzaSyCA2hSdjF-rRvq6xD3-s2h1xDZ1DGiMlx4",
    "authDomain": "broke-gas.firebaseapp.com",
    "databaseURL": "https://broke-gas-default-rtdb.firebaseio.com",
    "projectId": "broke-gas",
    "storageBucket": "broke-gas.appspot.com",
    "messagingSenderId": "759807890184",
    "appId": "1:759807890184:web:24349c11727e9e3bd252bd"
  }

firebase = pyrebase.initialize_app(config)

db = firebase.database()
>>>>>>> 1391c4afe75eb941a086b5dd2e44cdc8e3a847b1

#@app.route('/about')
#def about()
 #   form = gasUser()
  #  if form.validate_on_submit():
   #     return render_template('about.html',pageTitle ='User Info idk')
    #return render_template('index.html',pageTitle='BrokegAss')
from . import routes