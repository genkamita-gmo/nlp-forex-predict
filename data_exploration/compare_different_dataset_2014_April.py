# coding: utf-8
import pandas as pd
get_ipython().magic(u'pwd ')
df = pd.read_csv("*.csv")
df = pd.read_csv("DAT_NT_EURUSD_T_ASK_201704.csv")
df
df = pd.read_csv("DAT_NT_EURUSD_T_ASK_201704.csv",names=["index","date","price","zero"])
df
plot(df.price)
get_ipython().magic(u'pylab')
plot(df.price)
df.head()
df = pd.read_csv("DAT_NT_EURUSD_T_ASK_201704.csv",names=["index","date","price"],delimiter=";")
df = pd.read_csv("DAT_NT_EURUSD_T_ASK_201704.csv",names=["date","price","zero"],delimiter=";")
plot(df.price)
df.description
df.description = ""
df.description = "nt_t_ask"
df
get_ipython().magic(u'cd ../HISTDATA_COM_ASCII_EURUSD_T201704/')
df2 = pd.read_csv("DAT_ASCII_EURUSD_T_201704.csv")
df2.head()
df2 = pd.read_csv("DAT_ASCII_EURUSD_T_201704.csv",names=["timestamp","bid","ask","zero"])
figure
figure()
plot(df2.price)
df2.head()
plot(df2.bid)
df2.description ="ASCII_T_"
df.describe
df.description
df2.description
get_ipython().magic(u'save 1-32 compare_different_dataset.py')

# files with name "DAT_*_*_T_SOMETHING.csv" has datapoints by tickes at the order of one seconds.
# ASCII tends to have more datapoints
