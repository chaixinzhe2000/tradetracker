import argparse
import datetime
import pandas as pd
from argparse import RawDescriptionHelpFormatter
import collect
import show
from profit import profit

def main():
    # description of the command-line interface
    description = '\
This is a command-line interface (CLI) tool that helps you track your most recent stock trades.\n\
Copyright (c) 2020 Xinzhe Chai & Jinoo Hong\n'

    # getting current date
    curr_date = datetime.datetime.now().strftime("%x")

    # defining arguments
    parser = argparse.ArgumentParser(
        description=description, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('command', type=str,
                        help='choose from list of commands', choices=['log', 'profit', 'show'])
    parser.add_argument('ticker', nargs='?', type=str, help='add a ticker to the end of your trade show command to show trades just for that ticker')
    args = parser.parse_args()

    # deciding command from command line arguments
    arg_command = args.command
    if arg_command == 'log':
        collect.new_entry()
    elif arg_command == 'profit':
        profit()
    elif arg_command == 'show':
        if args.ticker == None:
            show.show_trades()
        else:
           if check_ticker_input(args.ticker.upper()):
               show.show_trade_for_ticker(args.ticker.upper())
        
# modified version of check_ticker_input from collect.py. I feel like we should have a input validity file that has all the input checking there (input checking 
# shouldnt be in collect.py cus we needa check input for other things as well)
def check_ticker_input(ticker):
    if collect.connect():
        print('Checking ticker validity...     ', end="", flush=True)
        if len(ticker) < 1 or len(ticker) > 10 or collect.check_validity(ticker) is False:
            print('INVALID TICKER INPUT. trade show ' + ticker + ' command FAILED', end="", flush=True)
            return False    
    else:
        if len(ticker) < 1 or len(ticker) > 10:
            print('INVALID TICKER INPUT. trade show ' + ticker + ' command FAILED', end="", flush=True)
            return False
    return True

if __name__ == "__main__":
    main()