import argparse
import datetime
from argparse import RawDescriptionHelpFormatter
        
# description of the command-line interface
description = '\
This is a command-line interface (CLI) tool that helps you track your most recent stock trades.\n\
Copyright (c) 2020 Xinzhe Chai -> https://xchai.me'

# getting current date
curr_time = datetime.datetime.now().strftime("%x")

# defining arguments
parser = argparse.ArgumentParser(
    description=description, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-t', '--ticker', required=True, metavar='TICKER', type=str, help='stock symbol of your trade (eg. MSFT)')
parser.add_argument('-o', '--optn', required=True, metavar='OPTN', type=str, choices=['buy', 'sell'], help='type of the trade ("buy" or "sell")')
parser.add_argument('-q', '--qty', required=True, metavar='QTY', type=float, help='quantity of the trade, in shares')
parser.add_argument('-d', '--date', metavar='DATE', type=str, default=curr_time, help='date of trade in MM/DD/YY format')
args = parser.parse_args()

# now, we have 4 arguments
print(args.ticker + ' ' + args.optn + ' ' + args.date + ' ' + str(args.qty))

