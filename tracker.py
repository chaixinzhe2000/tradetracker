import argparse
import datetime
import pandas as pd
from argparse import RawDescriptionHelpFormatter

def main():
    # description of the command-line interface
    description = '\
    This is a command-line interface (CLI) tool that helps you track your most recent stock trades.\n\
    Copyright (c) 2020 Xinzhe Chai (https://xchai.me)\n\n\
    Available commands include:\n\
    new       Enter new trade data\n\
    delete    Enter old trade data, including chai'

    # getting current date
    curr_date = datetime.datetime.now().strftime("%x")

    # defining arguments
    parser = argparse.ArgumentParser(
        description=description, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('command', type=str,
                        help='choose from list of commands', choices=['new', 'delete', 'profit'])
    args = parser.parse_args()

    # deciding command from command line arguments
    arg_command = args.command
    if arg_command == 'new':
        new_entry()
    elif arg_command == 'delete':
        print('feature awaiting implementation')
    elif arg_command == 'profit':
        print('profit feature awaiting implementation')

def new_entry():
    entry_correct = False
    ticker, trade_type, price, quantity, date = None, None, None, None, None
    print("Please enter the trade you wish to record")

    while entry_correct is False:
        # maybe check with API to see? use yfinance
        ticker = input(
            'Enter stock symbol of your trade (eg. MSFT): ').upper() or ticker
        while len(ticker) < 1:
            ticker = input(
                'Please re-enter a valid stock symbol (eg. MSFT): ').upper()
        # limit input to "buy" or "sell"
        trade_type = input(
            'Enter type of the trade ("buy" or "sell"): ').capitalize() or trade_type
        while (trade_type != 'Buy') and (trade_type != 'Sell'):
            trade_type = input(
                'Please re-enter type of the trade using "buy" or "sell": ').upper()
        # need to check input type
        price = input(
            'Enter execution price of the trade, in dollars: ') or price
        quantity = input(
            'Enter the quantity of the trade, in shares: ') or quantity
        # need to check input type
        date = input(
            "Enter the date of trade in MM/DD/YY format: ") or date
            
        # order summary
        print('----------------------------------------------------------------------------')
        print('You have excecuted the following order: ' + trade_type +
              ' ' + str(quantity) + ' ' + ticker + ' @ ' + str(price) + ' on ' + date)
        print('----------------------------------------------------------------------------')
        entry_confirmation = input("is the information correct? (y/n): ")
        if (entry_confirmation == 'y') or (entry_confirmation == 'Y'):
            entry_correct = True
            # add data into the excel
            print('\nWriting to trading_data.xlsx...')
            print('\nOrder "' + trade_type +
                  ' ' + str(quantity) + ' ' + ticker + ' @ ' + str(price) + ' on ' + date + '" is recorded in trading_data.xlsx')
            print("Thank you for using Stock Tracker. Good luck on your next trade.")
        else:
            print("\nLet's do this again. You can press ENTER to skip those correct entries.")
            print('-----------------------------------------------------------------------')

if __name__ == "__main__":
    main()
