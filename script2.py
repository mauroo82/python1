import requests
import json
import datetime
from time import sleep
from os import system, name
#from prettytable import PrettyTable

minuti = 2 # tempo di aggiornamento
#58f3d6d388msh17839452635e3bcp114681jsn2d383f4a6859

MSFTMIval = float(184.5575)
ENIMIval = float(9.05487)
ISPMIval = float(1.65648)

class colors: # You may need to change color settings in iPython
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'

headers = {
    'x-rapidapi-host': "yahoo-finance-free.p.rapidapi.com",
    'x-rapidapi-key': "7584a90205msh7517ee1b6eb0bd8p15e282jsnba3f26a7582a"
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
    querystring = {"region":"IT","lang":"it","symbols":"msft.mi"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    price = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
    return price

def Perc(valore_attuale, valore_acquisto):
    p1a = float(valore_attuale)
    p1c = round(100 * (p1a - valore_acquisto) / p1a, 2)
    return '{} %'.format(p1c)

def main():
    while True:
            now = datetime.datetime.now()
            print (now.strftime("%d-%m-%Y %H:%M:%S"))
            price1z =  Perc(funz_MSFTMI(), MSFTMIval)
            #price1 = funz_MSFTMI()
            #price1a = float(price1.replace(',','.'))
            #price1a = (price1.replace(",", "."))
            #price1b = float(price1a)

            #price1 = float(funz_MSFTMI().replace(',','.'))
            #price1a = round(100* (price1 - MSFTMIval)/ price1, 2)
            #price1z = '{} %'.format(price1a)

            #price2 = float(funz_ISPMI().replace(',','.'))
            #price2a = round(100* (price1 - MSFTMIval)/ price1, 2)
            #price2z = '{} %'.format(price1a)

            #price3 = float(funz_ENIMI().replace(',','.'))
            #price3a = round(100* (price3 - MSFTMIval)/ price1, 2)
            #price3z = '{} %'.format(price1a)



            #price5 = funz_LYPGF()
            #price6 = funz_VGWLF()
            print(colors.YELLOW + '---------------------------------FINECO---------------------------------', colors.ENDC)
            print('{:<50}{:<15}{:<15}'.format('MICROSOFT','MSFT.MI', price1z))
            #print('{:<50}{:<15}{:<15}'.format('INTESA SAN PAOLO','ISP.MI',price2))
            #print('{:<50}{:<15}{:<15}'.format('ENI','ENI.MI',price3))
            print(colors.YELLOW + '------------------------------------------------------------------------', colors.ENDC)
            print('')
            print(colors.YELLOW + '---------------------------------DIRECTA--------------------------------', colors.ENDC)
            #print('{:<50}{:<15}{:<15}'.format('Lyxor MSCI World Information Technology',' LYPG.F',price5))
            #print('{:<50}{:<15}{:<15}'.format('Vanguard FTSE All-World UCITS ETF ',' VGWL.F',price6))
            print(colors.YELLOW + '------------------------------------------------------------------------', colors.ENDC)

            sleep(450 * minuti)
            clear()
if __name__ == "__main__":
    main()

