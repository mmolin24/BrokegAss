from bs4 import BeautifulSoup
import requests
from pprint import pprint
import zipcodes

zipCode =  input("enter zip code: ")
validZip = zipcodes.matching(zipCode)


if len(validZip) == 0:
    print("He")
else:
    print(validZip)
    print("hello idiots")
    URL = "http://www.baltimoregasprices.com/GasPriceSearch.aspx?fuel=A&qsrch="+ zipCode

    response = requests.get(URL)
    #pprint(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(id='rrlow_0')

    if results is not None:
    

        address_elems = results.find('dl',class_='address')
        price_elems = results.find('div',class_='price_num')
        update_elems = results.find('div',class_='tm')

        print(address_elems.text.strip())
        print(price_elems.text)
        print(update_elems.text)










