from . import app
from . import retrieval
from . import googleDirections
import pyrebase
import json
from twilio.rest import Client 
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


# the firebase database information will be pulled from here
config = {
    "apiKey": "AIzaSyCA2hSdjF-rRvq6xD3-s2h1xDZ1DGiMlx4",
    "authDomain": "broke-gas.firebaseapp.com",
    "databaseURL": "https://broke-gas-default-rtdb.firebaseio.com",
    "projectId": "broke-gas",
    "storageBucket": "broke-gas.appspot.com",
    "messagingSenderId": "759807890184",
    "appId": "1:759807890184:web:24349c11727e9e3bd252bd"
}

# the firebase configuration is initialized
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# the text message information is declared
account_sid = 'AC0dd9645c50bba7a8fc065e57f2b02a65' 
auth_token = 'd712f0d1a6075f1b43b4d944aff10a58' 
client = Client(account_sid, auth_token) 


class LoginForm(FlaskForm):
    zip_code = IntegerField('zip_code',validators=[DataRequired()])
    phone_number = IntegerField('phone_number',validators=[DataRequired()])
    fuel_type = StringField('fuel_type', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

def sendMessage(user):
    # user has phone number, zip code, and fuel type
    # nearestGas has address, price, last updated
    # link has the link to navigation
    nearestGas = nearGasStation(user["zip-code"], user["fuel-type"])
    link = hyperLink(ret["address"])
    str = "Hey! Gas near {zip} is cheapest at {price}, Last updated {update}\nClick the link to go! {link}".format(zip=user["zip-code"],price=nearestGas["price"], update=nearestGas["update"], link=link)
    return str


@app.route('/')
def hello_world():
    form=LoginForm()
    if form.validate_on_submit():

        # create the dict with the form information
        temp = {
            "phone-number": form.phone_number.data,
            "zip-code": form.zip_code.data,
            "fuel-type": form.fuel_type.data
        }

        # place the dict into the database
        db.child("users").child(temp["phone-number"]).set(temp)

        # send the user the message
        msg = client.messages.create(to=temp["phone-number"], messaging_service_sid="MG2caa1803320b6894a8bcfff5256dc24a",
                                 body=sendMessage(temp))
    return render_template('form.html', title="HomePage", form=form)


@app.route('/form')
def about():

    form=LoginForm()
    if form.validate_on_submit():

        # create the dict with the form information
        temp = {
            "phone-number": form.phone_number.data,
            "zip-code": form.zip_code.data,
            "fuel-type": form.fuel_type.data
        }

        # place the dict into the database
        db.child("users").child(temp["phone-number"]).set(temp)

        # send the user the message
        msg = client.messages.create(to=temp["phone-number"], messaging_service_sid="MG2caa1803320b6894a8bcfff5256dc24a",
                                 body=sendMessage(temp))
    return render_template('form.html', title="HomePage", form=form)

@app.route('/user/<username>')
def profile(username):
    return 'this gas user is {}'.format(username)

@app.route('/feed')
def feed():
    return ''
    
