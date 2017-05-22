from math import log, sqrt
from numpy import mean, arange

def compound_interest(price_list):
 return [log(v / price_list[abs(i-1)]) for i, v in enumerate(price_list)]

def variance(price_list):
 compoundinterest = compound_interest(price_list)
# avg = mean(compoundinterest)
 return sum( [x**2 for x in compoundinterest] ) / float(len(compoundinterest))

def normalized_variance(price_list):
    var = variance(price_list)
    samples = len(price_list)
    return var * (1000/samples)  # normalising volatility to 1000 ticks

def volatility(price_list):
 vol = sqrt( normalized_variance(price_list) )
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
