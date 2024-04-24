### Library Imports
import pandas as pd
import yfinance as yf 
import warnings
warnings.filterwarnings('ignore')

### Function to Import Stock Data
def import_stock_data(tickers, start_date):
    # Check if tickers is a list or a single ticker string
    if isinstance(tickers, list):
        data = yf.download(tickers, start = start_date)[['Close', 'High', 'Low']]
    else:
        data = yf.download(tickers, start = start_date)[['Close', 'High', 'Low']]
        data = pd.DataFrame(data)

    # Reset index to make 'Date' a column instead of index
    data.reset_index(inplace = True)
    data['Date'] = pd.to_datetime(data['Date'])

    return data