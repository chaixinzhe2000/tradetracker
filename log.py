import pandas as pd
import numpy as np
import interface_with_excel as iwe

# BUG: can sell when does not hold position (maybe we need a short version)

def log_to_excel(ticker, trade_type, price, quantity, date):
    df = iwe.get_df()
    helper_df = iwe.get_helper_df()

    net_effect = calc_net_effect(trade_type, price, quantity)
    total_shares_holding = calc_total_shares_holding(helper_df,ticker,trade_type,quantity)
    ticker_total_value, ticker_average = calc_ticker_values(helper_df,ticker,trade_type,price,quantity,total_shares_holding)
    realized_profit = calc_realized_profit(helper_df, ticker, trade_type, total_shares_holding, price, quantity)
    data = [ticker, date, trade_type, price, \
            quantity, net_effect, total_shares_holding, ticker_total_value, ticker_average, realized_profit]
    data_to_log = pd.DataFrame([data], columns=['TICKER', 'DATE', 'BUY/SELL', 'PRICE', 'VOLUME', \
                                                'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT'])
    df = df.append(data_to_log, ignore_index=True)
    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    ###TRY TO GET ALL COLUMNS INTO 2 DECIMAL PLACES WHEN TALKING ABOUT CURRENCY
    df.to_excel(iwe.excel_file_name, index=False)
    print(df)

    #update dictionary_of_latest_trades
    iwe.update_to_dict_of_latest_trades_for_each_ticker(data_to_log)

def calc_net_effect(trade_type, price, quantity):
    net_effect = float(np.round(float(price) * float(quantity), 2))
    if trade_type == 'BUY':
        net_effect = '-' + f"{net_effect:.2f}"
    else:
        net_effect = '+' + f"{net_effect:.2f}"
    return net_effect

def calc_total_shares_holding(df, ticker_symbol, trade_type, quantity):
    previous_shares = 0
    for row in df.iterrows():
        # optional performance consideration: this would be slower when we have large amount of data, but a good approach indeed.
        if row[1]['TICKER'] == ticker_symbol:
            previous_shares = row[1]['TOTAL_SHARES_HOLDING']
    if previous_shares == 0:
        return quantity
    else:
        if trade_type == 'BUY':
            current_shares = previous_shares + quantity
        else:
            current_shares = previous_shares - quantity
        return current_shares

def calc_ticker_values(df, ticker_symbol, trade_type, price, quantity, total_share_quantity):
    previous_value = 0
    for row in df.iterrows():
        # optional performance consideration: this would be slower when we have large amount of data, but a good approach indeed.
        if row[1]['TICKER'] == ticker_symbol:
            previous_value = row[1]['TICKER_TOTAL_VALUE']
            previous_average = row[1]['AVERAGE_PRICE']
    if previous_value == 0:
        return np.round(price * quantity, 2), price
    else:
        # need to add a SHORT version, and check validity
        if trade_type == 'BUY':
            current_value = previous_value + price * quantity
            current_average = np.round(current_value / total_share_quantity, 2)
        else:
            current_value = previous_value - previous_average * quantity
            current_average = 0 if total_share_quantity == 0 else previous_average
        return current_value, current_average

def calc_realized_profit(df, ticker_symbol, trade_type, total_shares_holding, price, quantity):
    if trade_type == 'BUY':
        return None
    else: 
        for row in df.iterrows():
            if row[1]['TICKER'] == ticker_symbol:
                previous_average_buy_cost = row[1]['AVERAGE_PRICE']
        return (price - previous_average_buy_cost) * quantity
                