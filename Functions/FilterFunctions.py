### Function for CCI and RSI to Filter based on Buying/Selling Thresholds
def filter_indicators(indicator_df, upper_threshold, lower_threshold, tickers):
    # Set new filtered df to the input indicator_df
    filtered_df = indicator_df.copy()
    
    # Create empty lists for buy/sell signals
    buy_signals = []
    sell_signals = []
    
    # Loop through each ticker and apply filtering logic
    for ticker in tickers:
        indicator_value = filtered_df[ticker].iloc[-1]  # Get the last indicator value for the ticker
        
        # Check if CCI value is within the specified thresholds
        if indicator_value >= lower_threshold and indicator_value <= upper_threshold:
            del filtered_df[ticker]  # Remove ticker from the filtered DataFrame
        else:
            # Update buy/sell lists with tickers meeting the conditions
            if indicator_value >= upper_threshold:
                buy_signals.append((ticker, indicator_value))  # Append tuple of (ticker, CCI value) to buy_signals
            else:
                sell_signals.append((ticker, indicator_value))  # Append tuple of (ticker, CCI value) to sell_signals
    
    # Print the filtered DataFrame (optional)
    # print(filtered_df.tail(5))
    
    # Print tickers with potential buy and sell signals
    print("Tickers with potential BUY signals:")
    for ticker, indicator_value in buy_signals:
        print(f"{ticker}: {round(indicator_value, 6)}")
    
    print("\nTickers with potential SELL signals:")
    for ticker, indicator_value in sell_signals:
        print(f"{ticker}: {round(indicator_value, 6)}")

    return filtered_df

# Function Call:
filtered_df = filter_indicators(cci_df, 100, -100, cci_df.columns)
filtered_df.tail(5)