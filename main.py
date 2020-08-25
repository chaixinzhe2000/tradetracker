import argparse
import datetime
import pandas as pd
from argparse import RawDescriptionHelpFormatter
from collect import new_entry
from show import show_trades
from profit import profit

def main():
    # description of the command-line interface
    description = '\
This is a command-line interface (CLI) tool that helps you track your most recent stock trades.\n\
Copyright (c) 2020 Xinzhe Chai & Jinoo Hong\n\n\
Available commands include:\n\
  new       Enter new trade data\n\
  profit    Check profit for individual ticker'

    # getting current date
    curr_date = datetime.datetime.now().strftime("%x")

    # defining arguments
    parser = argparse.ArgumentParser(
        description=description, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('command', type=str,
                        help='choose from list of commands', choices=['log', 'profit', 'show'])
    args = parser.parse_args()

    # deciding command from command line arguments
    arg_command = args.command
    if arg_command == 'log':
        new_entry()
    elif arg_command == 'profit':
        profit()
    elif arg_command == 'show':
        show_trades()

if __name__ == "__main__":
    main()