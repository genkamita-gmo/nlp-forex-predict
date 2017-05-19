# coding: utf-8
import pandas as pd
import numpy as np
import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

pairs = pd.read_csv("good-pair-year.txt",names=["pair"])
column_names =  np.asarray(["date","title"])
dataset = pd.read_csv(input_filename, names=column_names)

volatility = dict()
for pair in pairs.pair:
    filename = pair + "-vol.txt"
    volatility[pair] =   pd.read_csv(filename,names=["date","volatility"])

#pairs = ["USDJPY"] # for tests
#dates =["20070109"]
pairs = pairs.pair
dates  = dataset.date

for pair in pairs:
    temp_column = np.full( len(dataset.date), np.nan )
    index = 0
    for date in dates:
	print("date:",date, "pair:", pair )
        vol = volatility[pair].query("date == " + "'" + str(date) + "'").volatility.tolist()
        print vol
        try:
           try:
               print("vol: #### LIST ####")
               temp_column[index] = vol[0]
           except:
               print("vol: #### SCALAR ####")
               temp_column[index] = vol
        except:
            print("vol: ----UNAVAILABLE----") 
        print temp_column[index]
 	index += 1
    dataset[ pair] = temp_column
dataset.to_csv(output_filename)
