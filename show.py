import pandas as pd
import numpy as np

def show_trades():
    #this function prints the latest trades from each of the tickers that we currently hold shares of
    excel_file = './trading_data.xlsx'
    df = pd.read_excel(excel_file)

    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')

    #make a dictionary of all the tickers we have: (key is ticker name and value is their trade row) (if key is same, value is overwritten so we go from oldest to newest trades)
    dict_of_trades = dict()
    for row in df.iterrows():
        dict_of_trades[row[1]['TICKER']] = row[1]

    #put these dictionary values into a datafram so we can output in the appropriate format (rows are trades and columns are trade details)
    new_df_to_print = pd.DataFrame(dict_of_trades.values(), columns=['TICKER', 'DATE', 'BUY/SELL', 'PRICE', 'VOLUME', \
                                                'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT'])
    print(new_df_to_print)