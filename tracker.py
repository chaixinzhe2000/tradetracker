import pandas as pd

df = pd.read_csv('/trade-tracker/trading_data.csv')

tickers = ['CODX', 'AMZN', 'SRNE']

# this is index masking 
filt = (df['Ticker'] == 'CODX') | (df['Ticker'] == 'SRNE')
filt_2 = df['Ticker'].isin(tickers)
filt_3 = df['Buy/Sell'].str.contains('Buy', na = False)
high_profit = (df['Net Profit'] > 0)
df.columns = [x.upper() for x in df.columns]
df.columns = df.columns.str.replace(' ', '_')

# create new column
df['FULL_NAME'] = df['first'] + ' ' + df['last']
df.drop(columns=['first', 'last'], inplace = True)

# delete specific filter
filt = df['last'] == 'Doe'
df.drop(index = df[filt].index)
df.drop(index = 4)

# counting
df['FULL_NAME'].count()

# to date time
df['DATE'] = pd.to_datetime(df['DATE'])

# sorting
df.sort_values(by=['PRICE', 'VOLUME'], ascending='True')
df.nlargest(10, 'PRICE')

# locating specific targets
df.loc[2, ['TICKER', 'DATE']] = ['CODX', '20-Jul'] 
print(df[filt])

# alternative way to express
print(df.loc[high_profit, ['NET_PROFIT', 'PRICE', 'BUY/SELL']])

print(df.loc[filt_2, ['DATE', 'PRICE']])
print(df.loc[filt_3])


 