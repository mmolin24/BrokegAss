from bs4 import BeautifulSoup
import requests
from pprint import pprint
import zipcodes

def nearGasStation(zipCode):
    
    validZip = zipcodes.matching(zipCode)
    stringGas = "No available gas near you"

    if len(validZip) == 0:
        print("zip does not exist!")
    else:      
        URL = "http://www.baltimoregasprices.com/GasPriceSearch.aspx?fuel=A&qsrch="+ zipCode

        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find(id='rrlow_0')

        if results is not None:
            address_elems = results.find('dl',class_='address')
            price_elems = results.find('div',class_='price_num')
            update_elems = results.find('div',class_='tm')
            stringGas = address_elems.text.strip() + '\n' + price_elems.text.strip() + '\n' + update_elems.text.strip()

    station ={
        "address": address_elems, 
        "price": 
        "update":
        ""
    } 

    return station

def main():
    zipCodeIn =  input("enter zip code: ")

    gasStation = nearGasStation(zipCodeIn)
    print(gasStation)



main()





