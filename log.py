import pandas as pd
import numpy as np

def log_to_excel(ticker, trade_type, price, quantity, date):
    excel_file = './trading_data.xlsx'
    df = pd.read_excel(excel_file)

    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')

    net_effect = calc_net_effect(trade_type, price, quantity)
    total_shares_holding = calc_total_shares_holding(df,ticker,trade_type,quantity)
    data = [ticker, date, trade_type, price, \
            quantity, net_effect, total_shares_holding, None, None, None]
    data_to_log = pd.DataFrame([data], columns=['TICKER', 'DATE', 'BUY/SELL', 'PRICE', 'VOLUME', \
                                                'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT'])
    df = df.append(data_to_log, ignore_index=True)
    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    ###TRY TO GET ALL COLUMNS INTO 2 DECIMAL PLACES WHEN TALKING ABOUT CURRENCY
    df.to_excel(excel_file, index=False)
    print(df)

def calc_net_effect(trade_type, price, quantity):
    net_effect = float(np.round(float(price) * float(quantity), 2))
    if trade_type == 'BUY':
        net_effect = '-' + f"{net_effect:.2f}"
    else:
        net_effect = '+' + f"{net_effect:.2f}"
    return net_effect

def calc_total_shares_holding(df, ticker_symbol, trade_type, quantity):
    previous_shares = None
    for row in df.iterrows():
        #df.iterrows outputs row which is a tuple: (index, row data from df), so row[1] gives access to actual row data from df
        if row[1]['TICKER'] == ticker_symbol:
            previous_shares = row[1]['TOTAL_SHARES_HOLDING']
    
    if previous_shares is None:
        return quantity
    else:
        if trade_type == 'BUY':
            current_shares = previous_shares + quantity
        else:
            current_shares = previous_shares - quantity
        return current_shares


    ###WE WANT CUMULATIVE AND USE INDEX MASKING TO FIND LATEST
