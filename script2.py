import requests
import json
import datetime
from time import sleep
from os import system, name
#from prettytable import PrettyTable

minuti = 2 # tempo di aggiornamento
#5XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class colors: # You may need to change color settings in iPython
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
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
    price = (respdict['price']['regularMarketPrice']['fmt'])
    return price

def funz_ISPMI():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"region":"IT","symbol":"ISP.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    price = (respdict['price']['regularMarketPrice']['fmt'])
    return price

def funz_ENIMI():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"region":"IT","symbol":"ENI.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    price = (respdict['price']['regularMarketPrice']['fmt'])
    return price



def funz_LYPGF():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"region":"IT","symbol":"LYPG.F"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    price = (respdict['price']['regularMarketPrice']['fmt'])
    return price

def funz_VGWLF():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"region":"IT","symbol":"VGWL.F"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    price = (respdict['price']['regularMarketPrice']['fmt'])
    return price

def main():
    while True:
            now = datetime.datetime.now()
            print (now.strftime("%d-%m-%Y %H:%M:%S"))
            price1 = funz_MSFTMI()
            price2 = funz_ISPMI()
            price3 = funz_ENIMI()

            price5 = funz_LYPGF()
            price6 = funz_VGWLF()
            print(colors.YELLOW + '---------------------------------FINECO---------------------------------', colors.ENDC)
            print('{:<50}{:<15}{:<15}'.format('MICROSOFT','MSFT.MI',price1))
            print('{:<50}{:<15}{:<15}'.format('INTESA SAN PAOLO','ISP.MI',price2))
            print('{:<50}{:<15}{:<15}'.format('ENI','ENI.MI',price3))
            print(colors.YELLOW + '------------------------------------------------------------------------', colors.ENDC)
            print('')
            print(colors.YELLOW + '---------------------------------DIRECTA--------------------------------', colors.ENDC)
            print('{:<50}{:<15}{:<15}'.format('Lyxor MSCI World Information Technology',' LYPG.F',price5))
            print('{:<50}{:<15}{:<15}'.format('Vanguard FTSE All-World UCITS ETF ',' VGWL.F',price6))
            print(colors.YELLOW + '------------------------------------------------------------------------', colors.ENDC)

            sleep(5 * minuti)
            clear()
if __name__ == "__main__":
    main()
