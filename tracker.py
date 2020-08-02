import argparse
import datetime
import pandas as pd
from argparse import RawDescriptionHelpFormatter

# description of the command-line interface
description = '\
This is a command-line interface (CLI) tool that helps you track your most recent stock trades.\n\
Copyright (c) 2020 Xinzhe Chai -> https://xchai.me'

# getting current date
curr_date = datetime.datetime.now().strftime("%x")

# defining arguments
parser = argparse.ArgumentParser(
    description=description, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-t', '--ticker', required=True, metavar='TICKER',
                    type=str, help='stock symbol of your trade (eg. MSFT)')
parser.add_argument('-o', '--optn', required=True, metavar='OPTN', type=str,
                    choices=['buy', 'sell'], help='type of the trade ("buy" or "sell")')
parser.add_argument('-q', '--qty', required=True, metavar='QTY',
                    type=float, help='quantity of the trade, in shares')
parser.add_argument('-p', '--price', required=True, metavar='PRICE',
                    type=float, help='execution price of the trade, in dollars')
parser.add_argument('-d', '--date', metavar='DATE', type=str,
                    default=curr_date, help='date of trade in MM/DD/YY format')
args = parser.parse_args()

# collecting data from command line arguments
ticker = args.ticker.upper()
trade_type = args.optn.capitalize()
price = args.price
quantity = args.qty
date = args.date

# now, we have 4 arguments
print('You have excecuted the following order: ' + trade_type +
      ' ' + str(quantity) + ' ' + ticker + ' @ ' + str(price) + ' on ' + date)

entry_correct = False

while entry_correct is False:
    entry_confirmation = input("is the information correct? (y/n): ")
    if (entry_confirmation == 'y') or (entry_confirmation == 'Y'):
        entry_correct = True
        # add data into the excel
        print('\nWriting to trading_data.xlsx...')
        print('\nOrder "' + trade_type +
        ' ' + str(quantity) + ' ' + ticker + ' @ ' + str(price) + ' on ' + date + '" is recorded in trading_data.xlsx')
    else:
        print("\nNo worries, let's do this again.")
        # maybe check with API to see? use yfinance
        ticker = input('Enter stock symbol of your trade (eg. MSFT): ').upper()
        while len(ticker) < 1:
            ticker = input('Please re-enter a valid stock symbol (eg. MSFT): ').upper()
        # limit input to "buy" or "sell"
        trade_type = input('Enter type of the trade ("buy" or "sell"): ').capitalize()
        while (trade_type != 'Buy') and (trade_type != 'Sell'):
            trade_type = input('Please re-enter type of the trade using "buy" or "sell": ').capitalize()
        # need to check input type
        price = input('Enter execution price of the trade, in dollars: ')
        quantity = input('Enter the quantity of the trade, in shares: ')
        # need to check input type
        date = input("Enter the date of trade in MM/DD/YY format: ") or curr_date

print("Thank you for using Stock Tracker CLI. Good luck on your next trade!")

