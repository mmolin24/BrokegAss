from bs4 import BeautifulSoup
import requests
from pprint import pprint
import zipcodes

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




