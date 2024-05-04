### Library Imports
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
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


### Compute RSI for Multiple Tickers 
def calculate_rsi(data, periods, tickers):
    rsi_df = pd.DataFrame(index = data.index)
    rsi_vals = {}

    for t in tickers:
        # Calculate price changes for each ticker
        data[f'{t}_Price Change'] = data['Close'][t].diff()
        # Separate gains and losses
        data[f'{t}_Gain'] = data[f'{t}_Price Change'].apply(lambda x: x if x > 0 else 0)
        data[f'{t}_Loss'] = data[f'{t}_Price Change'].apply(lambda x: abs(x) if x < 0 else 0)
        # Calculate average gains and losses over the period
        data[f'{t}_Avg Gain'] = data[f'{t}_Gain'].rolling(window = periods).mean()
        data[f'{t}_Avg Loss'] = data[f'{t}_Loss'].rolling(window = periods).mean()
        # Calculate RS (Relative Strength)
        data[f'{t}_RS'] = data[f'{t}_Avg Gain'] / data[f'{t}_Avg Loss']
        # Calculate RSI using the formula: RSI = 100 - (100 / (1 + RS))
        data[f'{t}_RSI'] = 100 - (100 / (1 + data[f'{t}_RS']))
        # Append RSI column to the DataFrame
        rsi_df[t] = data[f'{t}_RSI']
        # Append last RSI value to rsi_vals dictionary
        rsi_vals[t] = data[f'{t}_RSI'].iloc[-1]

    return rsi_df, rsi_vals


### MACD Function for Multiple Stocks
def calculate_macd(tickers, df):
    # Initialize empty DataFrame to store MACD data with correct columns
    macd_df = pd.DataFrame(index = df.index, columns=tickers[::-1])  # Reverse the tickers list
    macd_vals = {}

    # Loop for MACD calculation and df population
    for t in tickers:
        # Calculate 12-day Exponential Moving Averages (EMA)
        ema_12 = df['Close'][t].ewm(span = 12, adjust = False).mean()
        # Calculate 26-day Exponential Moving Averages (EMA)
        ema_26 = df['Close'][t].ewm(span = 26, adjust = False).mean()
        # Calculate MACD line (12-day EMA minus 26-day EMA)
        macd = ema_12 - ema_26
        # Calculate 9-day EMA of MACD line (Signal line)
        signal_line = macd.ewm(span=9, adjust=False).mean()
        # Add MACD and Signal columns to the DataFrame
        macd_df[t] = macd
        macd_df[f"{t}_Signal"] = signal_line
        # Append last MACD value to macd_vals dictionary
        macd_vals[t] = macd_df[t].iloc[-1]

    return macd_df, macd_vals


### Function to Calculate CCI
def calculate_cci(df, window):
    # empty list init
    cci_last_row = []

    # Calculate Typical Price (TP) = (High + Low + Close) / 3
    typ_price = (df['High'] + df['Low'] + df['Close']) / 3 
    # Simple Moving Average (SMA) of TP
    sma = typ_price.rolling(window = window).mean()  
    # Mean Deviation (MD) = absolute difference between the TP and the SMA
    mean_dev = (typ_price - sma).abs().rolling(window=window).mean()  
    # Calculate Commodity Channel Index (CCI) = (TP - SMA) / (0.015 * MD)
    cci_df = (typ_price - sma) / (0.015 * mean_dev)
    
    # Append last two row values to cci_vals list
    cci_last_row.extend(cci_df.iloc[-1:].values)
    # extract just the final row of values
    cci_vals = np.array(cci_last_row[0])

    return cci_df, cci_vals


### Calculate Single Ticker ADX
def get_ADX(data, window):
    # Calculate True Range (TR)
    tr1 = pd.DataFrame(data['High'] - data['Low'])
    tr2 = pd.DataFrame(abs(data['High'] - data['Close'].shift(1)))
    tr3 = pd.DataFrame(abs(data['Low'] - data['Close'].shift(1)))
    frames = [tr1, tr2, tr3]
    data['TR'] = pd.concat(frames, axis='columns', join='inner').max(axis='columns')

    # Calculate the Directional Movement (DM +/-) = Current High/Low - Previous High/Low (if both are positive, otherwise zero)
    for i in range(1, len(data)):
        # Build positive and negative DM columns
        pdm = data.iloc[i]['High'] - data.iloc[i - 1]['High']
        ndm = data.iloc[i - 1]['Low'] - data.iloc[i]['Low']
    
        data.at[i, 'PDM'] = pdm if pdm > 0 else 0
        data.at[i, 'NDM'] = abs(ndm) if ndm > 0 else 0

    # Smooth TR, PDM, and NDM using 14-period EMA
    data['TR_Smooth'] = data['TR'].ewm(span=window, adjust=False).mean()
    data['PDM_Smooth'] = data['PDM'].ewm(span=window, adjust=False).mean()
    data['NDM_Smooth'] = data['NDM'].ewm(span=window, adjust=False).mean()

    # Calculate the Directional Indicators (DI+ and DI-) = (PDM / Smoothed TR) * 100 and = (NDM / Smoothed TR) * 100
    data['DI+'] = (data['PDM_Smooth'] / data['TR_Smooth']) * 100
    data['DI-'] = (data['NDM_Smooth'] / data['TR_Smooth']) * 100

    # Calculate the Directional Index (DX) = (abs(DI+ - DI-) / (DI+ + DI-)) * 100
    data['DX'] = (abs(data['DI+'] - data['DI-']) / (data['DI+'] + data['DI-'])) * 100

    # Calculate Average Directional Index (ADX) = 14-period EMA of DX
    data['ADX'] = data['DX'].ewm(span=window, adjust=False).mean()

    return data


### Function for ADX Multiple Tickers
def adx_mult_tickers(data, tickers, window=14):
    adx_dfs = []  # Initialize a list to store DataFrames for each ticker's ADX values

    for t in tickers:
        # Extract data for the specific ticker using the MultiIndex
        single_ticker_data = data.loc[:, (slice(None), t)]
        single_ticker_data.columns = single_ticker_data.columns.droplevel(1)  # Drop the second level of the columns index
        single_ticker_adx = get_ADX(single_ticker_data, window=window)

        # Create a DataFrame for the current ticker's ADX, DI+, and DI- values
        ticker_adx_df = pd.DataFrame({
            (t, 'ADX'): single_ticker_adx['ADX'],
            (t, 'DI+'): single_ticker_adx['DI+'],
            (t, 'DI-'): single_ticker_adx['DI-']
        })

        # Append the DataFrame to the list
        adx_dfs.append(ticker_adx_df)

    # Concatenate all DataFrames in the list to create the final adx_df DataFrame
    adx_df = pd.concat(adx_dfs, axis=1)

    return adx_df


### Plot Indicator Function
def plot_function(data, indicator_df, tickers, indicator_type):
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Filter stock_data and indicator_df based on start_date
    start_date = pd.Timestamp('2024-01-01')  # Assuming start_date is '2024-01-01'
    filtered_stock_data = data[data['Date'] >= start_date]
    filtered_indicator_data = indicator_df[indicator_df.index.isin(filtered_stock_data.index)]

    # Plot Stocks Analyzed
    fig = plt.figure(figsize = (10, 6))
    ax = fig.add_subplot(2, 1, 1)
    ax.set_xticklabels([])
    plt.plot(filtered_stock_data['Date'], filtered_stock_data['Close'], lw = 1, label = tickers)
    plt.title('Stock Price Chart')
    plt.ylabel('Close Price')
    plt.xlabel('Dates')
    plt.grid(True)

    # Add Indicator Subplot
    bx = fig.add_subplot(2, 1, 2)
    for t in tickers:
        plt.plot(filtered_stock_data['Date'], filtered_indicator_data[t], lw = 1, label = t)
    plt.title(indicator_type + ' Values')
    plt.legend(loc=2, prop={'size': 9.5})
    plt.ylabel('Calculated ' + indicator_type)
    plt.xlabel('Dates')
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=30)
    plt.tight_layout()
    plt.show()