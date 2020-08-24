# we could possibly use this file to store commands that will help us interface with excel. for example:
# - read the excel file and output a df
# - give me a list of all the tickers we currently have shares of
# - etc.

# this way, if we want to access the same data across different files and functions, we can all call that data from here (makes it easier to change code, and less work for us)
# we can also use this to hold for example, a dictionary or set or wtv that stores all the tickers we own. and it can also store the latest trades for each ticker. this way we dont need to run through the whole list of trades every time we want to find the latest trade for a given ticker

#lmk what u think of this chai!

import pandas as pd
import numpy as np

excel_file_name = './trading_data.xlsx'

def get_df():
    df = pd.read_excel(excel_file_name)
    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    return df
    