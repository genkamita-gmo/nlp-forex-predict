from math import log, sqrt
from numpy import mean, arange

def compound_interest(price_list):
 return [log(v / price_list[abs(i-1)]) for i, v in enumerate(price_list)]

def variance(price_list):
 compoundinterest = compound_interest(price_list)
 avg = mean(compoundinterest)
 return sum( [(x - avg)**2 for x in compoundinterest] ) / float(len(compoundinterest))

def volatility(price_list):
 vol = sqrt( variance(price_list) )
 return vol

if __name__ == "__main__":
    #import pandas as pd
    #df = pd.read_csv("HISTDATA_COM_ASCII_AUDJPY_M12006/DAT_ASCII_AUDJPY_M1_2006.csv-date", delimiter=";",
    #names=["date", "time", "open", "high", "low", "close", "volume"])
    #list_of_prices = df.open
    list_of_prices = arange(1.0,4.0)
    print(list_of_prices)
    vol = volatility(list_of_prices)
    print(vol)
