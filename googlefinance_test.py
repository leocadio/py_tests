# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 12:10:00 2017

@author: User
"""

import googlefinance.client as gfc

# Dow Jones
param = {
    'q': ".DJI", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "INDEXDJX", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "5Y" # Period (Ex: "1Y" = 1 year)
}
# get price data (return pandas dataframe)
df = gfc.get_price_data(param)


print(df)