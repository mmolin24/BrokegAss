import json
import pyrebase
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
app.config['SECRET_KEY']='downbadsquadgg'
from . import routes