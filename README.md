# Stock Trading Key Indicators Analysis

This repository contains implementations of various stock trading indicators and a full analysis using 50 stock tickers in Python. The project is structured into the following folders:

### 1. IndicatorAnalysis

#### MACD.ipynb
MACD (Moving Average Convergence Divergence) calculates the difference between a short-term and a long-term exponential moving average (EMA) of an asset's price. The notebook first analyzes 50 stock tickers and then computes MACD values using the `calculate_macd` function. A filtering method is applied to generate buying or selling trends based on the MACD values using the following logic:
  - Buy condition: 
    - A buy condition is met if the MACD line of the current period is greater than the Signal line and the MACD line of the previous period is less than the Signal line of the previous period.
  - Define sell condition: 
    - A sell condition is met if the MACD line of the current period is less than the Signal line and the MACD line of the previous period is greater than the Signal line of the previous period.

Finally, the `plot_function()` is used to display selected tickers after applying the filter.

#### ADX.ipynb
ADX (Average Directional Index) quantifies the strength of a trend without indicating its direction. The notebook analyzes 50 stock tickers and computes ADX values using the `adx_mult_tickers()` function. A filtering method is applied to generate buying or selling trends based on the ADX values. Then filtering is applied using the following logic:
  - Buy Signal Conditions:
    - ADX is rising (indicating increasing trend strength) and crosses above a threshold (30).
    - (DI+) crosses above (DI-), indicating a potential uptrend.
  - Sell Signal Conditions:
    - ADX is falling (indicating weakening trend strength) and crosses below a threshold (20).
    - (DI-) crosses above (DI+), indicating a potential downtrend.

Finally, the `plot_function()` is used to display selected tickers after applying the filter.

#### CCI.ipynb
CCI (Commodity Channel Index) identifies overbought or oversold conditions in an asset. The notebook analyzes 50 stock tickers and computes CCI values using the `calculate_cci` function. A filtering method is applied to generate buying or selling trends based on the CCI values. The logic for filtering includes the following: 
  - Below -100 - Oversold conditions, price has moved significantly below its average, suggesting a potential downtrend or extended period of weakness, generating a potential SELL signal
  - Above +100 - Overbought conditions, upward trend is beginning, generating a potential BUY signal. 

Finally, the `plot_function()` is used to display selected tickers after applying the filter.

#### RSI.ipynb
RSI (Relative Strength Index) measures recent price changes to evaluate overbought or oversold conditions in an asset. The notebook analyzes 50 stock tickers and computes RSI values using the `calculate_rsi` function. A filtering method is applied to generate buying or selling trends based on the RSI values. The logic for filtering includes the following: 
  - Below 30 - indicate oversold conditions which generates a potential BUY signal, expect the price to rebound or correct upward after being oversold from downward selling pressure
  - Above 70 - indicate overbought conditions which generates a potential SELL signal.
    
Finally, the `plot_function()` is used to display selected tickers after applying the filter.

#### Indicator Values Verification
A link to verify indicator values is provided [here](https://aiolux.com/reports/analytics-technical-indicators?scroll=pills-tab&symbol=GOOG&tab_name=macd&utf8=%E2%9C%93).

### 2. Functions

#### IndicatorFunctions.py

This folder contains all the necessary functions to perform the Indicator Analysis as shown below:

- `getTickers()`: Contains the function to load in desired stock ticker Date, Close, High, and Low pricing data using the Yahoo Finance (yfinance) library.

- `calculate_rsi()`: Calculates the Relative Strength Index (RSI) value for each ticker based on price changes. RSI is calculated using the average of upward price changes and downward price changes over a specified period, typically 14 days. The formula for RSI involves calculating the Relative Strength (RS) as the ratio of average gains to average losses, and then converting RS into the RSI value using the formula: RSI = 100 - (100 / (1 + RS)).

- `calculate_cci()`: Computes the Commodity Channel Index (CCI) value for each ticker, which measures the relationship between an asset's price, its moving average, and its standard deviation. CCI is used to identify overbought or oversold conditions in an asset. The CCI formula involves calculating the Typical Price (TP) as the average of high, low, and close prices, the Simple Moving Average (SMA) of TP, the Mean Deviation (MD) as the absolute difference between TP and SMA, and then applying the CCI formula: CCI = (TP - SMA) / (0.015 * MD).

- `calculate_macd()`: Computes the Moving Average Convergence Divergence (MACD) value for each ticker by comparing short-term (12-day) and long-term (26-day) exponential moving averages (EMA). The MACD line is calculated as the difference between these EMAs, while the Signal line is a 9-day EMA of the MACD line. The MACD histogram is computed as the difference between the MACD line and the Signal line.

- `get_ADX()`: Calculates the Average Directional Index (ADX) to quantify trend strength for each ticker. ADX is part of the Directional Movement System and measures the strength of a trend, whether it's an uptrend or a downtrend, without indicating the direction of the trend itself. The ADX calculation involves computing the Positive Directional Movement (+DM), Negative Directional Movement (-DM), True Range (TR), Smoothed +DM, Smoothed -DM, and the Directional Index (DX) = (abs(DI+ - DI-) / (DI+ + DI-)) * 100. Finally, the rolling 14-day EMA of the DX is taken to derive the ADX.

- `adx_mult_tickers()`: Computes the Average Directional Index (ADX) values for multiple tickers, allowing for trend strength analysis across a range of assets. This function utilizes the ADX calculation logic for individual tickers but extends it to handle multiple tickers simultaneously.

- `plot_function()`: Filters stock and indicator data based on the selected start date and generates plots illustrating close prices and computed indicator values over time. This function enables visual analysis of stock price movements and technical indicator trends, aiding in decision-making for traders and investors.

### 3. FilterFunctions

This folder contains the multi-use function to perform the filtering on the CCI and RSI as shown below:
- `filter_indicators()`: The function first checks to see the indicator value is within the specified thresholds, and if not the ticker is filtered out. The remaining tickers and then sorted into buy/sell lists provided tickers meet the specified conditions specific to the RSI and CCI indicators.


