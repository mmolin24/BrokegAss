import json
import pyrebase
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
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

from . import routes