import yfinance as yf
import datetime
import urllib.request
from log import log_to_excel

# checking internet connection
def connect(host="https://www.google.com/"):
    try:
        urllib.request.urlopen(host)
        # print("Connected to internet")
        return True
    except:
        # print("Failed to connect to internet")
        return False

# this python file implements the log command of the tracker
def new_entry():
    entry_correct = False
    ticker, trade_type, price, quantity, date = None, None, None, None, datetime.datetime.now().strftime("%x")
    print("Please enter the trade you wish to record")

    while entry_correct is False:
        # finished validation
        ticker = input(
            'Enter stock symbol of your trade: ').upper() or ticker
        ticker = check_ticker_input(ticker)
        # finished type checking
        trade_type = input(
            'Enter type of trade ("buy" or "sell"): ').upper() or trade_type
        trade_type = check_type_input(trade_type)
        # need to convert to certain float
        price = input(
            'Enter execution price of the trade, in dollars: ') or price
        price = check_price_input(price)
        # finished type checking
        quantity = input(
            'Enter the quantity of the trade, in shares: ') or quantity
        quantity = check_quantity_input(quantity)
        # finished type checking
        date = input(
            "Enter the date of trade in MM/DD/YY format: ") or date
        date = check_date(date)
            
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
            log_to_excel(ticker,trade_type,price,quantity,date)
            print('\nOrder "' + trade_type +
                  ' ' + str(quantity) + ' ' + ticker + ' @ ' + str(price) + ' on ' + date + '" is recorded in trading_data.xlsx')
            print("Thank you for using Stock Tracker. Good luck on your next trade.")
        else:
            print("\nLet's do this again. You can press ENTER to skip those correct entries.")
            print('----------------------------------------------------------------------------')

# when connected to internet, will check ticker validity
def check_ticker_input(ticker):
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

def check_validity(ticker):
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

def check_type_input(trade_type):
    while (trade_type != 'BUY') and (trade_type != 'SELL'):
        trade_type = input('Please re-enter type of the trade, using "buy" or "sell": ').upper()
    return trade_type

def check_price_input(number):
    while check_float(number) is False:
        price = input(
            'Please re-enter a valid execution price of the trade, in dollars: ')
        number = price
    number = round(float(number), 2)
    return number

def check_quantity_input(number):
    while check_float(number) is False:
        quantity = input(
            'Please re-enter a valid quantity of the trade, in shares: ')
        number = quantity
    return number

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

def check_float(number):
    try:  
        float(number)
        res = True
        if float(number) < 0:
            res = False
    except: 
        res = False
    return res