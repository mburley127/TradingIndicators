### Library Imports
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

### Plot Indicator Function
### Plot Indicator Functions
def plot_function(data, indicator_df, tickers):
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Filter stock_data and mult_adx based on start_date
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

    # Add ADX Subplot
    bx = fig.add_subplot(2, 1, 2)
    for t in tickers:
        plt.plot(filtered_stock_data['Date'], filtered_indicator_data[t], lw = 1, label = t)
    plt.title('ADX Values')
    plt.legend(loc=2, prop={'size': 9.5})
    plt.ylabel('Calculated ADX')
    plt.xlabel('Dates')
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=30)
    plt.tight_layout()
    plt.show()