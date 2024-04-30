# Stock Trading Key Indicators Analysis

This repository contains implementations of various stock trading indicators, as well as a full analysis using 50 stock tickers in Python. The indicator and analysis folders included are:

1. **IndicatorAnalysis**
   - `MACD.ipynb`: MACD (Moving Average Convergence Divergence) calculates the difference between a short-term and a long-term exponential moving average (EMA) of an asset's price. The project first analyzes 50 stock tickers, and then runs the `calculate_macd` function to output the computed MACD values. Using the computed MACD values, a filtering method is applied in order to produce buying or selling trends (expand here on logic). Finally, the `plot_function()` is used to display a selected number of tickers chosen after the filter is applied. 
   - `ADX.ipynb`: ADX (Average Directional Index) is used to quantify the strength of a trend. It's part of the Directional Movement System and measures the strength of a trend, whether it's an uptrend or a downtrend, without indicating the direction of the trend itself. The project first analyzes 50 stock tickers, and then runs the `adx_mult_tickers()` function to output the computed ADX values. Using the computed ADX values, a filtering method is applied in order to produce buying or selling trends (expand here on logic). Finally, the `plot_function()` is used to display a selected number of tickers chosen after the filter is applied. 
   - `CCI.ipynb`: CCI (Commodity Channel Index) calculates the relationship between an asset's price, its moving average, and its standard deviation. The CCI is used to identify overbought or oversold conditions in an asset and can help traders determine potential reversal points. The project first analyzes 50 stock tickers, and then runs the `calculate_cci` function to output the computed CCI values. Using the computed CCI values, a filtering method is applied in order to produce buying or selling trends by performing the following:
     Below -100 - Oversold conditions, price has moved significantly below its average, suggesting a potential downtrend or extended period of weakness, generating a potential SELL signal.
     Above +100 - Overbought conditions, upward trend is beginning, generating a potential BUY signal.
Finally, the `plot_function()` is used to display a selected number of tickers chosen after the filter is applied. 
   - `RSI.ipynb`: RSI (Relative Strength Index) measures the magnitude of recent price changes to evaluate overbought or oversold conditions in an asset. It's a momentum oscillator that ranges from 0 to 100 and is often used to identify potential trend reversals or confirm the strength of a trend. The project first analyzes 50 stock tickers, and then runs the `calculate_rsi` function to output the computed RSI values. Using the computed RSI values, a filtering method is applied in order to produce buying or selling trends by performing the following:
     Below 30 - indicate oversold conditions which generates a potential BUY signal, expect the price to rebound or correct upward after being oversold from downward selling pressure
     Above 70 - indicate overbought conditions which generates a potential SELL signal
Finally, the `plot_function()` is used to display a selected number of tickers chosen after the filter is applied. 
  
     Indicator Values verification: https://aiolux.com/reports/analytics-technical-indicators?scroll=pills-tab&symbol=GOOG&tab_name=macd&utf8=%E2%9C%93

2. **Functions**
   - `IndicatorFunctions.py`: This folder contains all the necessary functions to perform the Indicator Analysis as shown below:
        - `getTickers()`: Contains the function to load in desired stock ticker Date, Close, High, and Low pricing data using the yahoo finance (yfinance) folder.
        - `calculate_rsi()`: Contains the function to calculate the RSI value. The calculation is done by first computing the price changes for each ticker and seperating into gain/loss columns. See the "Whitepapers" folder for the full indicator calculation.
        - `calculate_cci()`:
        - `calculate_macd()`:
        - `get_ADX()`:
        - `adx_mult_tickers()`:
        - `plot_function()`: The function initially filters the stock data frame and indicator data frame based on the selected start date to plot the desired data. Next, the function generates a plot illustrating the close prices of each ticker versus the date. Additionally, the function generates a plot demonstrating the computed values for each indicator versus the date.
