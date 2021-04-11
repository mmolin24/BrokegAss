from bs4 import BeautifulSoup
import requests
from pprint import pprint
import zipcodes

def nearGasStation(zipCode,fuelType):
    
    validZip = zipcodes.matching(zipCode)

    if len(validZip) == 0:
        address_elems = "zip code not valid"
        price_elems = ""
        update_elems = ""
    else:      
       # URL = "http://www.baltimoregasprices.com/GasPriceSearch.aspx?fuel=A&qsrch="+ zipCode
        URL = "http://www.baltimoregasprices.com/GasPriceSearch.aspx?fuel=" +fuelType+ "&qsrch="+ zipCode    
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find(id='rrlow_0')

        if results is not None:
            address_elems = results.find('dl',class_='address').text.strip()
            price_elems = results.find('div',class_='price_num').text.strip()
            update_elems = results.find('div',class_='tm').text.strip()
        
        else:
            address_elems = "No available gas stations near you!"
            price_elems = ""
            update_elems = ""

    station ={
        "address": address_elems,
        "price": price_elems,
        "update": update_elems,
    } 

    return station

def main():
    zipCodeIn =  input("enter zip code: ")

    gasStation = nearGasStation(zipCodeIn,"C")
    print(gasStation)



main()





