import pandas as pd
import numpy as np

def log_to_excel(ticker, trade_type, price, quantity, date):
    excel_file = './trading_data.xlsx'
    df = pd.read_excel(excel_file)
    net_effect = calc_net_effect(trade_type, price, quantity)
    data = [ticker, date, trade_type, price, \
            quantity, net_effect, None, None, None, None]
    data_to_log = pd.DataFrame([data], columns=['TICKER', 'DATE', 'BUY/SELL', 'PRICE', 'VOLUME', \
                                                'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT'])
    df = df.append(data_to_log, ignore_index=True)
    numerical_columns = ['PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    df.to_excel(excel_file, index=False)
    print(df)

def calc_net_effect(trade_type, price, quantity):
    net_effect = float(np.round(float(price) * float(quantity)))
    if trade_type == 'BUY':
        net_effect = '-' + f"{net_effect:.2f}"
    else:
        net_effect = '+' + f"{net_effect:.2f}"
    return net_effect