import pandas as pd

df = pd.read_csv('/trade-tracker/trading_data.csv')

tickers = ['CODX', 'AMZN', 'SRNE']
# this is index masking 
filt = (df['Ticker'] == 'CODX') | (df['Ticker'] == 'SRNE')
filt_2 = df['Ticker'].isin(tickers)
filt_3 = df['Buy/Sell'].str.contains('Buy', na = False)
high_profit = (df['Net Profit'] > 0)
print(df[filt])
# alternative way to express
print(df.loc[high_profit, ['Net Profit', 'Price', 'Buy/Sell']])

print(df.loc[filt_2, ['Date', 'Price']])
print(df.loc[filt_3])
