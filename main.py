import argparse
import datetime
import pandas as pd
from argparse import RawDescriptionHelpFormatter
from collect import new_entry

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
                        help='choose from list of commands', choices=['log', 'delete', 'profit'])
    args = parser.parse_args()

    # deciding command from command line arguments
    arg_command = args.command
    if arg_command == 'log':
        new_entry()
    elif arg_command == 'delete':
        print('feature awaiting implementation')
    elif arg_command == 'profit':
        print('profit feature awaiting implementation')

if __name__ == "__main__":
    main()