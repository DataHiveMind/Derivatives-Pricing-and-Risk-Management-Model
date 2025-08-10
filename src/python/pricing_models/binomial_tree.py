"""
src/python/pricing_models/binomial_tree.py

Purpose:
The purpose of this module is to implement the binomial tree model for option pricing. This model provides a discrete-time framework for valuing options by simulating the underlying asset's price movements over time.

Aim:
The aim of this module is to provide a clear and efficient implementation of the binomial tree model, allowing users to price European and American options with various underlying asset characteristics and market conditions.
"""

import pandas as pd 
import numpy as np 
import scipy as sp 
import statsmodels.api as sm

#-----------------------------------------------------------
# Binomail Tree Functions
#-----------------------------------------------------------

def binomial_tree(S0: float, K: float, T: float, r: float, 
    sigma: float, n: int, option_type: str = 'call') -> float:
    """
    Purpose: Binomial tree option pricing model.

    Parameters:
    S0 : float
        Initial stock price
    K : float
        Option strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate (annualized)
    sigma : float
        Volatility of the underlying stock (annualized)
    n : int
        Number of time steps in the binomial tree
    option_type : str
        Type of option ('call' or 'put')

    Returns:
    float
        The estimated option price
    """
    dt = T / n  # Time step
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor
    p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    # Initialize asset prices at maturity
    asset_prices = np.zeros(n + 1)
    for i in range(n + 1):
        asset_prices[i] = S0 * (u ** (n - i)) * (d ** i)

    # Initialize option values at maturity
    if option_type == 'call':
        option_values = np.maximum(0, asset_prices - K)
    else:
        option_values = np.maximum(0, K - asset_prices)

    # Backward induction
    for j in range(n - 1, -1, -1):
        option_values = np.exp(-r * dt) * (p * option_values[:-1] + (1 - p) * option_values[1:])

    return option_values[0]

#--------------------------------------------------------------
# Example Usage
#--------------------------------------------------------------

if __name__ == "__main__":
    S0 = 100  # Initial stock price
    K = 100   # Option strike price
    T = 1     # Time to maturity (in years)
    r = 0.05  # Risk-free interest rate (annualized)
    sigma = 0.2  # Volatility of the underlying stock (annualized)
    n = 100   # Number of time steps in the binomial tree
    option_type = 'call'  # Type of option ('call' or 'put')

    option_price = binomial_tree(S0, K, T, r, sigma, n, option_type)
    print(f"The estimated {option_type} option price is: {option_price}")