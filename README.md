# Stock Trading Key Indicators Analysis

This repository contains implementations of various stock trading indicators, as well as a full analysis using 30 stock tickers in Python. The indicator and analysis folders included are:

1. **Indicators**
   - `getTickers.ipynb`: Contains the function to load in desired stock ticker Date, Close, High, and Low pricing data using the yahoo finance (yfinance) folder.
   - `plotIndicators.ipynb`: The function initially filters the stock data frame and indicator data frame based on the selected start date to plot the desired data. Subsequently, the function generates a plot illustrating the close prices of each ticker versus the date. Additionally, the function generates a plot demonstrating the computed values for each indicator versus the date.
   - `MACD.ipynb`: MACD (Moving Average Convergence Divergence) calculates the difference between a short-term and a long-term exponential moving average (EMA) of an asset's price. The function includes a complete is used to identify changes in the strength, direction, momentum, and duration of a trend in an asset's price. See "Whitepapers" folder for full calculation.
   - `ADX.ipynb`: ADX (Average Directional Index) is used to quantify the strength of a trend. It's part of the Directional Movement System and measures the strength of a trend, whether it's an uptrend or a downtrend, without indicating the direction of the trend itself. See "Whitepapers" folder for full calculation. See "Whitepapers" folder for full calculation.
   - `CCI.ipynb`: CCI (Commodity Channel Index) calculates the relationship between an asset's price, its moving average, and its standard deviation. The CCI is used to identify overbought or oversold conditions in an asset and can help traders determine potential reversal points.See "Whitepapers" folder for full calculation.
   - `RSI.ipynb`: RSI (Relative Strength Index) measures the magnitude of recent price changes to evaluate overbought or oversold conditions in an asset. It's a momentum oscillator that ranges from 0 to 100 and is often used to identify potential trend reversals or confirm the strength of a trend. See "Whitepapers" folder for full calculation.

2. **IndicatorAnalysis**
   - `IndicatorAnalysis`: Contains the implementation of the

3. **Whitepapers**
   - `IndicatorAnalysis.pdf`: Contains the .pdf of the full calculation of each indicator (MACD, RSI, CCI, ADX).
