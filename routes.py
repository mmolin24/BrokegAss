from . import app
import pyrebase
import json
from twilio.rest import Client 
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from bs4 import BeautifulSoup
import requests
import zipcodes

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
auth_token = '2bdcebb9fac76a3cd659a5a4314e5bd3' 
client = Client(account_sid, auth_token) 



def nearGasStation(zipCode,fuelType):
    
    # use zipcodes to validate the zipcode input
    validZip = zipcodes.matching(zipCode)

    # check if the zip code is available, if not set dummy values
    if len(validZip) == 0:
        address_elems = "zip code not valid!"
        price_elems = ""
        update_elems = ""
    else:      
       # using site to retrieve gas prices from the entire US
        URL = "http://www.baltimoregasprices.com/GasPriceSearch.aspx?fuel=" +fuelType+ "&qsrch="+ zipCode    
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find(id='rrlow_0')

        # searching and placing the correct values into their values for the schema
        if results is not None:
            address_elems = results.find('dl',class_='address').text.strip()
            price_elems = results.find('div',class_='price_num').text.strip()
            update_elems = results.find('div',class_='tm').text.strip()
        
        # if there's no gas stations in the area set it.
        else:
            address_elems = "No available gas stations near you!"
            price_elems = ""
            update_elems = ""

    # return schema 
    station ={
        "address": address_elems,
        "price": price_elems,
        "update": update_elems,
    } 

    return station


def hyperLink(address):
    if(address[0] == '&'):
        return "sad"

    addressSplit = address.split()
    stringDirection = addressSplit[0]

    for i in range(1,len(addressSplit)):
        if addressSplit[i] != '&':
            stringDirection += "+" + addressSplit[i]
        
    hyperLinkCreated = "https://www.google.com/maps/dir/?api=1&origin=Your+location&destination=" + stringDirection + "&travelmode=driving"

    return hyperLinkCreated


class MyForm(Form):
    zip_code = IntegerField('zip_code',validators=[DataRequired()])
    phone_number = IntegerField('phone_number',validators=[DataRequired()])
    fuel_type = StringField('fuel_type', validators=[DataRequired()])
    submit = SubmitField('Submit Form')
    

def sendMessage(user):
    # user has phone number, zip code, and fuel type
    # nearestGas has address, price, last updated
    # link has the link to navigation
    if user["fuel-type"][0] == "r" or user["fuel-type"][0] == "R":
        fuel = "A"
    elif user["fuel-type"][0] == "M" or user["fuel-type"][0] == "m":
        fuel = "B"
    elif user["fuel-type"][0] == "P" or user["fuel-type"][0] == "p":
        fuel = "C"
    else:
        fuel = "D"
    
    nearestGas = nearGasStation(user["zip-code"], fuel)
    link = hyperLink(nearestGas["address"])
    str = "Thanks for using BrokegAss! Gas near {zip} is cheapest at ${price}, Last updated {update}\nClick the link to go! {link}".format(zip=user["zip-code"],price=nearestGas["price"], update=nearestGas["update"], link=link)
    return str


@app.route('/', methods=('GET','POST'))
def submit():
    
    form=MyForm()
    if request.method == 'POST':
        
        # create the dict with the form information
        temp = {
            "phone-number": request.form.get("phone_number"),
            "zip-code": request.form.get("zip_code"),
            "fuel-type": request.form.get("fuel_type")
        }
        
        # place the dict into the database
        db.child("users").child(temp["phone-number"]).set(temp)
        
        # send the user the message
        msg = client.messages.create(to=temp["phone-number"], messaging_service_sid="MG2caa1803320b6894a8bcfff5256dc24a",
                                 body=sendMessage(temp))
        
        return redirect("/")

    return render_template('index.html', title="HomePage", form=form)

@app.route('/feed')
def feed():
    return ''
    
