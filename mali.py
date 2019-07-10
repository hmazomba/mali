# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:51:07 2019

@author: hmazo
"""

import pandas as pd
import numpy as np
import datetime 
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas_datareader as pdr
import datetime

df = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2006, 10, 1), end=datetime.datetime(2012,1,1))

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()


df_ohlc.reset_index(inplace=True)

#convert dates to mdates
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
 
#Moving Windows
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()


#plot axes
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()

#ax1.plot(df.index, df['Adj Close'])
#ax1.plot(df.index, df['100ma'])
#ax2.bar(df.index, df['Volume'])

#plt.show()

#How much a stock changes per day

#daily_close = aapldf[['Adj Close']]
#daily_pct_change = daily_close.pct_change()
#daily_pct_change.fillna(0, inplace=True)
#
#daily_log_returns = np.log(daily_close.pct_change() +1)
#print(daily_log_returns)

#print(daily_pct_change)