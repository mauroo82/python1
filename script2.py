import requests
import json
import datetime
from time import sleep
from os import system, name

minuti = 2 # tempo di aggiornamento
#xxxxxxxxxxxxxxxxxxxxxx

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def funz_MSFTMI():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"region":"IT","symbol":"MSFT.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    price = print(respdict['price']['regularMarketPrice']['fmt'])
    return price

def funz_ISPMI():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"region":"IT","symbol":"ISP.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    price = print(respdict['price']['regularMarketPrice']['fmt'])
    return price

def main():
    while True:
            now = datetime.datetime.now()
            print (now.strftime("%d-%m-%Y %H:%M:%S"))
            price1 = funz_MSFTMI()
            price2 = funz_ISPMI()
            print(price1)
            print(price2)
            sleep(5 * minuti)
            clear()
if __name__ == "__main__":
    main()
