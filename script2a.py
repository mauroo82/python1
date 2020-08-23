import requests
import json
import datetime
from time import sleep
from os import system, name
#from prettytable import PrettyTable

minuti = 60 # tempo di aggiornamento
#

MSFTMIval = float(184.5575)
ENIMIval  = float(9.0548)
ISPMIval  = float(1.6565)
CCC3DEval = float(41.6563)

IBTMSWval = float(194.18)
TNOWMIval = float(364.32)
CMODMIval = float(12.428)
VWRLMIval = float(79.55)
IBGLMIval = float(279.49)

headers = {
    'x-rapidapi-host': "yahoo-finance-free.p.rapidapi.com",
#mauro.arduini    'x-rapidapi-key': "xxxxxxxxxxxxxxxxx"
#chiara
    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxx"
#mauroo    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxx"
    }
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def funz_stockquery():
    url = "https://yahoo-finance-free.p.rapidapi.com/v6/finance/quote"
    querystring = {"region":"IT","lang":"it","symbols":"MSFT.MI,eni.mi,ISP.MI,CCC3.DE,IBTM.MI,TNOW.MI,CMOD.MI,VWRL.MI,IBGL.MI"} #max 10 symbols
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "regularMarketPrice" in respdict
    if(check == "False"):
        price = "nd"
    else:
        try:
            price0y = (respdict['quoteResponse']['result'][0]['regularMarketPrice'])
            price1y = (respdict['quoteResponse']['result'][1]['regularMarketPrice'])
            price2y = (respdict['quoteResponse']['result'][2]['regularMarketPrice'])
            price3y = (respdict['quoteResponse']['result'][3]['regularMarketPrice'])
            price4y = (respdict['quoteResponse']['result'][4]['regularMarketPrice'])
            price5y = (respdict['quoteResponse']['result'][5]['regularMarketPrice'])
            price6y = (respdict['quoteResponse']['result'][6]['regularMarketPrice'])
            price7y = (respdict['quoteResponse']['result'][7]['regularMarketPrice'])
            price8y = (respdict['quoteResponse']['result'][8]['regularMarketPrice'])
        except:
            price0y = "nd"
            price1y = "nd"
            price2y = "nd"
            price3y = "nd"
            price4y = "nd"
            price5y = "nd"
            price6y = "nd"
            price7y = "nd"
            price8y = "nd"

    return (price0y,price1y,price2y,price3y,price4y,price5y,price6y,price7y,price8y)

def funz_COVID():
    headers2 = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "7584a90205msh7517ee1b6eb0bd8p15e282jsnba3f26a7582a"
    }
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country":"Italy"}
    response = requests.request("GET", url, headers=headers2, params=querystring)
    # print(response.json)
    respjson = response.text
    respdict = json.loads(respjson)
    #print(respdict)
    check =  "cases" in respdict
    if(check == "False"):
        price = "nd"
    else:
        try:
            price = (respdict['response'][0]['cases']['new'])
            datecovid = (respdict['response'][0]['day'])
        except:
            price = "nd"
    return (price,datecovid)

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
    if value == 'nd':
        return '{} nd {}'.format(color_positive,color_end)
    elif value < 0:
        return '{}{}%{}'.format(color_negative,value,color_end)
    else:
        return '{}{}%{}'.format(color_positive,value,color_end)

def main():
    while True:
            now = datetime.datetime.now()
            print (now.strftime("%d-%m-%Y %H:%M:%S"))

            stock = funz_stockquery()
            price0z =  Perc(stock[0], MSFTMIval)
            price1z =  Perc(stock[1], ENIMIval)
            price2z =  Perc(stock[2], ISPMIval)
            price3z =  Perc(stock[3], CCC3DEval)

            price4z =  Perc(stock[4], IBTMSWval)
            price5z =  Perc(stock[5], TNOWMIval)
            price6z =  Perc(stock[6], CMODMIval)
            price7z =  Perc(stock[7], VWRLMIval)
            price8z =  Perc(stock[8], IBGLMIval)

            #price6 = funz_VGWLF()
            print(colors.YELLOW + '---------------------------------FINECO--------------------------------------', colors.ENDC)
            print('{:<50}{:<15}{:>20}'.format('MICROSOFT','MSFT.MI', numColor(price0z),''))
            print('{:<50}{:<15}{:>20}'.format('ENI','ENI.MI',numColor(price1z),''))
            print('{:<50}{:<15}{:>20}'.format('INTESA SAN PAOLO','ISP.MI',numColor(price2z),''))
            print('{:<50}{:<15}{:>20}'.format('COCA COLA','CCC3.FRA',numColor(price3z),''))

            print(colors.YELLOW + '-----------------------------------------------------------------------------', colors.ENDC)
            print('')
            print(colors.YELLOW + '---------------------------------DIRECTA-------------------------------------', colors.ENDC)
            print('{:<50}{:<15}{:>20}'.format('ETF US TB710 ISHARES','IBTM.MI',numColor(price4z),''))
            print('{:<50}{:<15}{:>20}'.format('LYXOR ETF MSCI WORLD INFORMATION TECH','TNOW.MI',numColor(price5z),''))
            print('{:<50}{:<15}{:>20}'.format('SOURCE BLOOMBERG COMMODITY UCI ','CMOD.MI',numColor(price6z),''))
            print('{:<50}{:<15}{:>20}'.format('Vanguard FTSE All-World UCITS ETF ','VWRL.MI',numColor(price7z),''))
            print('{:<50}{:<15}{:>20}'.format('ETF EUGOVBOND1530 IS','IBGL.MI',numColor(price8z),''))
            print(colors.YELLOW + '-----------------------------------------------------------------------------', colors.ENDC)
            print('')
            print(colors.YELLOW + '---------------------------------COVID19-------------------------------------', colors.ENDC)
            daticovid = funz_COVID()
            print('{:<50}{:<15}{:>12}'.format('NUOVI CASI - Italia',daticovid[1],daticovid[0]))
            print(colors.YELLOW + '-----------------------------------------------------------------------------', colors.ENDC)
            print('')


            sleep(10 * minuti)
            clear()
if __name__ == "__main__":
    main()
