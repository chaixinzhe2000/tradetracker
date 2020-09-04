# we could possibly use this file to store commands that will help us interface with excel. for example:
# - read the excel file and output a df
# - give me a list of all the tickers we currently have shares of
# - etc.

# this way, if we want to access the same data across different files and functions, we can all call that data from here (makes it easier to change code, and less work for us)
# we can also use this to hold for example, a dictionary or set or wtv that stores all the tickers we own. and it can also store the latest trades for each ticker. this way we dont need to run through the whole list of trades every time we want to find the latest trade for a given ticker

#lmk what u think of this chai!

import pandas as pd
import numpy as np
import pickle
import os

excel_file_name = './trading_data.xlsx'
excel_helper_file_name = './data_helper.xlsx'

def get_df():
    df = pd.read_excel(excel_file_name)
    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    return df

### Method using dictionary
# def update_to_dict_of_latest_trades_for_each_ticker(data_row):
#     dictionary_file_path = './dict_of_latest_trades_for_each_ticker.pickle'
#     dictionary_file_name = 'dict_of_latest_trades_for_each_ticker.pickle'
#     if os.path.getsize(dictionary_file_path) > 0:
#         dictionary = pickle.load(open(dictionary_file_name,"rb"))
#         if data_row['TOTAL_SHARES_HOLDING'] == 0:
#             dictionary.pop(data_row['TICKER'],None)
#         else:
#             dictionary[data_row['TICKER']] = data_row
#     else: 
#         dictionary = {data_row['TICKER']:data_row}
#     pickle.dump(dictionary,open(dictionary_file_name,'wb'))

### Method using second excel file (data_helper.xlsx)
def update_to_dict_of_latest_trades_for_each_ticker(data_row):
    df = get_helper_df()
    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    data_row[numerical_columns] = data_row[numerical_columns].apply(pd.to_numeric, errors='coerce')

    found_ticker_flag = False
    for i, row in df.iterrows():
        if row['TICKER'] == data_row.loc[0]['TICKER']:
            df.iloc[i] = data_row.iloc[0]
            new_df = df
            found_ticker_flag = True
            break

    if df.empty or found_ticker_flag == False:
        if (data_row.loc[0]['TOTAL_SHARES_HOLDING'] != 0):
            new_df = pd.concat([df,data_row])

    ###TRY TO GET ALL COLUMNS INTO 2 DECIMAL PLACES WHEN TALKING ABOUT CURRENCY
    new_df.to_excel(excel_helper_file_name, index=False)

def get_helper_df():
    df = pd.read_excel(excel_helper_file_name)
    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    return df

def get_latest_trade(ticker):
    df = get_helper_df()
    for i, row in df.iterrows():
        if row['TICKER'] == ticker:
            return row
    return None