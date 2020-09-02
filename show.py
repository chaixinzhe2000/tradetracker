import pandas as pd
import numpy as np
import interface_with_excel as iwe

def show_trades():
    #this function prints the latest trades from each of the tickers that we currently hold shares of
    df = iwe.get_df()

    #make a dictionary of all the tickers we have: (key is ticker name and value is their trade row) (if key is same, value is overwritten so we go from oldest to newest trades)
    dict_of_trades = dict()
    for row in df.iterrows():
        if row[1]['TOTAL_SHARES_HOLDING'] == 0:
            dict_of_trades.pop(row[1]['TICKER'],None)
        else:
            dict_of_trades[row[1]['TICKER']] = row[1]

    #put these dictionary values into a datafram so we can output in the appropriate format (rows are trades and columns are trade details)
    new_df_to_print = pd.DataFrame(dict_of_trades.values(), columns=['TICKER', 'DATE', 'BUY/SELL', 'PRICE', 'VOLUME', \
                                                'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT'])
    print(new_df_to_print)

def show_trade_for_ticker(ticker):
    #this function prints the total trade history of one particular ticker
    df = iwe.get_df()
    #go through the whole df and find all trades with that ticker
    data_to_print = []
    for row in df.iterrows():
        if row[1]['TICKER'] == ticker:
            data_to_print.append(row[1])

    print(data_to_print)
    df_to_print = pd.DataFrame(data_to_print,columns=['TICKER', 'DATE', 'BUY/SELL', 'PRICE', 'VOLUME', \
                                                'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT'])
    print(df_to_print)