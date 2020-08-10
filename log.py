import pandas as pd

def log_to_excel(ticker,trade_type,price,quantity,date):
    df = pd.read_excel('./trading_data.xlsx')
    data = [ticker,date,trade_type,price,quantity,1,1,1,1,1]
    data_to_log = pd.DataFrame([data], columns=['TICKER', 'DATE', 'BUY/SELL', 'PRICE', 'VOLUME', 'NET_EFFECT_TO_CASH', 'TOTAL_SHARES_HOLDING', 'TICKER_TOTAL_VALUE', 'AVERAGE_PRICE', 'REALIZED_PROFIT'])
    df = df.append(data_to_log, ignore_index=True)
    print(df)


    
