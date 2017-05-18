from __future__ import print_function
import volatility
import sys
import pandas as pd

input_file = sys.argv[1]
df = pd.read_csv(input_file, delimiter=";", 
    names=["date", "time", "open", "high", "low", "close", "volume"])

for day in df.date.unique():
    price = df.query( "date ==" + str(day)).open
    vol = volatility.volatility( price.as_matrix() )
    print(day, vol, sep=",")
