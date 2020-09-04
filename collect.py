import yfinance as yf
import datetime
import urllib.request
from log import log_to_excel
import interface_with_excel as iwe

# TODO: make sure rounding is exact

# this python file aims to collect the trade information from the users, and
# utilizes log.py to log the relavent data to trading_data.xlsx

# checking internet connection
def connect(host="https://www.google.com/"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# driver function: the new_entry() method will prompt users to enter their trade information,
# and check whether the input is valid or not by calling helper functions.
def new_entry():
    entry_correct = False
    ticker, trade_type, price, quantity, date = None, None, None, None, datetime.datetime.now().strftime("%x")
    print("Please enter the trade you wish to record")

    while entry_correct is False:
        # collecting ticker information
        ticker = input(
            'Enter stock symbol of your trade: ').upper() or ticker
        ticker = check_ticker_input(ticker)
        # get current_holding (current shares holding) to validify sell amount
        latest_trade = iwe.get_latest_trade(ticker)
        current_holding = -1 if latest_trade is None else latest_trade['TOTAL_SHARES_HOLDING']
        # collecting trade type (buy or sell)
        trade_type = input(
            'Enter type of trade ("buy" or "sell"): ').upper() or trade_type
        trade_type = check_type_input(trade_type, current_holding)
        # collecting trade price information
        price = input(
            'Enter execution price of the trade, in dollars: ') or price
        price = check_price_input(price)
        # collecting trade quantity
        quantity = input(
            'Enter the quantity of the trade, in shares (type "all" for sell all): ') or quantity
        quantity = check_quantity_input(quantity, trade_type, current_holding)
        # collecting trade date
        date = input(
            "Enter the date of trade in MM/DD/YY format, press ENTER to use current date: ") or date
        date = check_date(date)
            
        # printing order summary
        print('----------------------------------------------------------------------------')
        print('You have excecuted the following order: ' + trade_type +
              ' ' + str(quantity) + ' ' + ticker + ' @ ' + "%0.2f" %price + ' on ' + date)
        print('----------------------------------------------------------------------------')
        # confirming trade with user
        entry_confirmation = input("is the information correct? (y/n): ")
        if (entry_confirmation == 'y') or (entry_confirmation == 'Y'):
            # writing trade data to excel by calling helper function
            print('\nWriting to trading_data.xlsx...')
            log_to_excel(ticker,trade_type,price,quantity,date)
            print('\nOrder "' + trade_type +
                  ' ' + str(quantity) + ' ' + ticker + ' @ ' + "%0.2f" %price + ' on ' + date + '" is recorded in trading_data.xlsx')
            another_trade = input("Do you want to log another trade? (y/n): ")
            if another_trade == 'y' or another_trade == 'Y':
                print("\nStart logging the next trade...")
                # reinitializing the input data
                ticker, trade_type, price, quantity, date = None, None, None, None, datetime.datetime.now().strftime("%x")
            else:
                entry_correct = True
                print("Thank you for using Stock Tracker. Good luck on your next trade.")
        else:
            print("\nLet's do this again. You can press ENTER to skip those correct entries.")
            print('----------------------------------------------------------------------------')

# when connected to internet, will check ticker validity
def check_ticker_input(ticker):
    if ticker == None or ticker == "":
        ticker = input('Please re-enter a valid stock symbol: ').upper()
    if connect():
        print('Checking ticker validity...     ', end="", flush=True)
        while len(ticker) < 1 or len(ticker) > 10 or check_validity(ticker) is False:
            print('[INVALID]')
            ticker = input('Please re-enter a valid stock symbol: ').upper()
            print('Checking ticker validity...     ', end="", flush=True)
        print('[VALID]')
    else:
        while len(ticker) < 1 or len(ticker) > 10:
            ticker = input('Please re-enter a valid stock symbol: ').upper()
    return ticker

# using yfinance module to check whether the ticker is valid
def check_validity(ticker):
    ###### WE STILL HAVE A BUG WHERE TICKERS LIKE SRNE OR UAL ARE NOT VALID
    ticker_validity = True
    try:
        yf.Ticker(ticker).info
    except IndexError:
        ticker_validity = False
    except KeyError:
        ticker_validity = False
    except ImportError:
        ticker_validity = False
    return ticker_validity

# type checking the trade type
def check_type_input(trade_type, current_holding):
    while (trade_type != 'BUY') and (trade_type != 'SELL') or (trade_type == 'SELL' and current_holding <= 0):
        trade_type = input('Please re-enter type of the trade, using "buy" or "sell" (you may be trying to sell a stock that you don\'t own yet): ').upper()
    return trade_type

# checking whether price is valid, and round it to 2 decimal places
def check_price_input(number):
    while check_float(number) is False:
        price = input(
            'Please re-enter a valid execution price of the trade, in dollars: ')
        number = price
    number = round(float(number), 2)
    return number

# checking whether quantity is valid, and round it to 2 decimal places
def check_quantity_input(quantity, trade_type, current_holding):
    if quantity.upper() == 'ALL' and trade_type == 'SELL':
        return current_holding
    while (check_float(quantity) is False) or (trade_type == 'SELL' and current_holding < float(quantity)):
        if quantity.upper() == 'ALL' and trade_type == 'SELL':
            return current_holding
        quantity = input(
            'Please re-enter a valid quantity of the trade, in shares (type "all" for sell all): ')
    return float(quantity)

# checking whether date follows the format
def check_date(date):
    date_correct = False
    # need to handle just pressing enter
    while (date_correct is False):
        try:
            datetime.datetime.strptime(date, '%m/%d/%y')
        except ValueError:
            date = input('Please re-enter a valid date of trade, in MM/DD/YY format: ')
        else:
            date_correct = True
    return date

# helper function for checking number validity
def check_float(number):
    try:  
        float(number)
        res = True
        if float(number) < 0:
            res = False
    except: 
        res = False
    return res