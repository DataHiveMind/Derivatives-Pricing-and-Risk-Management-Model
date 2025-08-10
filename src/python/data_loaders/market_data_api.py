"""
src/python/data_loaders/market_data_api.py

Purpose: This module provides an interface for fetching market data from various sources, including APIs and databases. It aims to standardize the process of data retrieval, making it easier to obtain and use market data for analysis and modeling.

Aim: The aim of this module is to provide a unified and efficient way to access market data, enabling users to seamlessly integrate data retrieval into their analysis workflows.
"""

import yfinance as yf 
import pandas as pd
import numpy as np 
import pandas_datareader as pdr
import pandas_datareader.data as web
import quantlib as ql

#---------------------------------------------------------
# Market Data Collection Function
#---------------------------------------------------------

def fetch_raw_market_data(symbol: str, start_date: str, end_date: str, chosen_source: str) -> pd.DataFrame:
    """
    Purpose: Fetch market data for a given symbol between specified dates.

    Parameters:
    symbol : str
        The stock or asset symbol to fetch data for
    start_date : str
        Start date for the data retrieval in 'YYYY-MM-DD' format
    end_date : str
        End date for the data retrieval in 'YYYY-MM-DD' format

    Returns:
    pd.DataFrame
        DataFrame containing market data with columns for date, open, high, low, close, and volume and save it into the data/raw folder
    """
    try:
        if chosen_source == 'yfinance':
            data = yf.download(symbol, start=start_date, end=end_date)
        elif chosen_source == 'pandas_datareader':
            data = pdr.data.get_data_yahoo(symbol, start=start_date, end=end_date)
        elif chosen_source == 'quantlib':
            # Placeholder for QuantLib data fetching
            data = pd.DataFrame()  # Replace with actual data fetching logic

        # Save the raw data to the data/raw folder
        data.to_csv(f"data/raw/{symbol}_raw.csv")
        return data

    except Exception as e:
        print(f"Error fetching market data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

#---------------------------------------------------------
# Market Data Processing Functions
#---------------------------------------------------------

def preprocess_market_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Purpose: Preprocess the raw market data for analysis.

    Parameters:
    data : pd.DataFrame
        The raw market data to preprocess

    Returns:
    pd.DataFrame
        The preprocessed market data
    """
    # Example preprocessing steps
    data = data.dropna()  # Remove missing values
    data['returns'] = data['close'].pct_change()  # Calculate returns
    return data


#------------------------------------------------------
# Technical Indicator Function
#------------------------------------------------------

def calculate_technical_indicators(data: pd.DataFrame, short_window: int, long_window: int) -> pd.DataFrame:
    """
    Purpose: Calculate technical indicators for the market data.

    Parameters:
    data : pd.DataFrame
        The market data to calculate indicators
    short_window : int
        The short window period for moving averages
    long_window : int
        The long window period for moving averages

    Returns:
    pd.DataFrame
        The market data with added technical indicators
    """
    # Simple Moving Averages
    data['SMA_short'] = data['close'].rolling(window=short_window).mean()  # 20-day Simple Moving Average
    data['SMA_long'] = data['close'].rolling(window=long_window).mean()  # 50-day Simple Moving Average

    # Exponential Moving Averages
    data['EMA_short'] = data['close'].ewm(span=short_window, adjust=False).mean()  # 20-day Exponential Moving Average
    data['EMA_long'] = data['close'].ewm(span=long_window, adjust=False).mean()  # 50-day Exponential Moving Average

    # RSI
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=long_window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=long_window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # MACD
    data['MACD'] = data['EMA_short'] - data['EMA_long']
    data['MACD_signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

    return data

#------------------------------------------------------
# Example Usage
#------------------------------------------------------

if __name__ == "__main__":
    # Fetch raw market data
    raw_data = fetch_raw_market_data("AAPL", "2020-01-01", "2020-12-31", "yfinance")

    # Preprocess the data
    processed_data = preprocess_market_data(raw_data)

    # Calculate technical indicators
    final_data = calculate_technical_indicators(processed_data)

    # Display the final data
    print(final_data.head())
