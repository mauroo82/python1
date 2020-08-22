import requests
import json
import datetime
from time import sleep
from os import system, name
#from prettytable import PrettyTable

minuti = 60 # tempo di aggiornamento
#xxxxxxxxxxxxxxxxxxxx

MSFTMIval = float(184.5575)
ENIMIval  = float(9.0548)
ISPMIval  = float(1.6565)

IBTMSWval = float(194.18)
TNOWMIval = float(364.32)
CMODMIval = float(12.428)
VWRLMIval = float(79.55)
IBGLMIval = float(279.49)



headers = {
    'x-rapidapi-host': "yahoo-finance-free.p.rapidapi.com",
    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def funz_MSFTMI():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"MSFT.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def funz_ENIMI():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"eni.mi"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def funz_ISPMI():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"ISP.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def funz_IBTMSW():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"IBTM.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def funz_TNOWMI():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"TNOW.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def funz_CMODMI():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"CMOD.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def funz_VWRLMI():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"VWRL.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price


def funz_IBGLMI():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"IBGL.MI"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def Perc(valore_attuale, valore_acquisto):
    if(valore_attuale == "nd"):
        return "nd"
    else:
        p1a = float(valore_attuale)
        p1c = round(100 * (p1a - valore_acquisto) / valore_acquisto, 2)
        #return '{} %'.format(p1c)
        return p1c

class colors:
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'


def numColor(value):
    color_positive = '\033[32m' # green
    color_negative = '\033[31m' # red
    color_end = '\033[m'
    if value < 0:
    #if '-' in value:
        return '{}{}%{}'.format(color_negative,value,color_end)
    else:
        return '{}{}%{}'.format(color_positive,value,color_end)

def main():
    while True:
            now = datetime.datetime.now()
            print (now.strftime("%d-%m-%Y %H:%M:%S"))
            price1z =  Perc(funz_MSFTMI(), MSFTMIval)
            price2z =  Perc(funz_ENIMI(), ENIMIval)
            price3z =  Perc(funz_ISPMI(), ISPMIval)

            price4z =  Perc(funz_IBTMSW(), IBTMSWval)
            price5z =  Perc(funz_TNOWMI(), TNOWMIval)
            price6z =  Perc(funz_CMODMI(), CMODMIval)
            price7z =  Perc(funz_VWRLMI(), VWRLMIval)
            price8z =  Perc(funz_IBGLMI(), IBGLMIval)




            #price6 = funz_VGWLF()
            print(colors.YELLOW + '---------------------------------FINECO--------------------------------------', colors.ENDC)
            print('{:<50}{:<15}{:>20}'.format('MICROSOFT','MSFT.MI', numColor(price1z),''))
            print('{:<50}{:<15}{:>20}'.format('ENI','ENI.MI',numColor(price2z),''))
            print('{:<50}{:<15}{:>20}'.format('INTESA SAN PAOLO','ISP.MI',numColor(price3z),''))

            print(colors.YELLOW + '-----------------------------------------------------------------------------', colors.ENDC)
            print('')
            print(colors.YELLOW + '---------------------------------DIRECTA-------------------------------------', colors.ENDC)
            print('{:<50}{:<15}{:>20}'.format('ETF US TB710 ISHARES','IBTM.MI',numColor(price4z),''))
            print('{:<50}{:<15}{:>20}'.format('LYXOR ETF MSCI WORLD INFORMATION TECH','TNOW.MI',numColor(price5z),''))
            print('{:<50}{:<15}{:>20}'.format('SOURCE BLOOMBERG COMMODITY UCI ','CMOD.MI',numColor(price6z),''))
            print('{:<50}{:<15}{:>20}'.format('Vanguard FTSE All-World UCITS ETF ','VWRL.MI',numColor(price7z),''))
            print('{:<50}{:<15}{:>20}'.format('ETF EUGOVBOND1530 IS','IBGL.MI',numColor(price8z),''))
            print(colors.YELLOW + '-----------------------------------------------------------------------------', colors.ENDC)

            sleep(10 * minuti)
            clear()
if __name__ == "__main__":
    main()

