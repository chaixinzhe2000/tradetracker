import yfinance as yf

# this python file implements the log command of the tracker
def new_entry():
    entry_correct = False
    ticker, trade_type, price, quantity, date = None, None, None, None, None
    print("Please enter the trade you wish to record")

    while entry_correct is False:
        # finished validation
        ticker = input(
            'Enter stock symbol of your trade (eg. MSFT): ').upper() or ticker
        ticker = check_ticker_input(ticker)
        # finished type checking
        trade_type = input(
            'Enter type of the trade ("buy" or "sell"): ').upper() or trade_type
        trade_type = check_type_input(trade_type)
        # need to convert to certain float
        price = input(
            'Enter execution price of the trade, in dollars: ') or price
        price = check_price_input(price)
        # finished type checking
        quantity = input(
            'Enter the quantity of the trade, in shares: ') or quantity
        quantity = check_quantity_input(quantity)
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
            print('----------------------------------------------------------------------------')

def check_ticker_input(ticker):
    print('Checking ticker validity...     ', end="", flush=True)
    while len(ticker) < 1 or len(ticker) > 10 or check_validity(ticker) is False:
        print('[INVALID]')
        ticker = input('Please re-enter a valid stock symbol (eg. MSFT): ').upper()
        print('Checking ticker validity...     ', end="", flush=True)
        check_validity(ticker)
    print('[VALID]')
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
    return number
        

def check_quantity_input(number):
    while check_float(number) is False:
        quantity = input(
            'Please re-enter a valid quantity of the trade, in shares: ')
        number = quantity
    return number

def check_float(number):
    try:  
        float(number)
        res = True
        if float(number) < 0:
            res = False
    except: 
        res = False
    return res