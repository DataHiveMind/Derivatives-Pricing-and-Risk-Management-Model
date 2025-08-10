"""
src/python/pricing_models/black_scholes.py

Purpose: Black-Scholes Model for Option Pricing

Aim: To provide a mathematical model for pricing European-style options.
"""
import scipy as sp 
import pandas as pd 
import numpy as np 
import statsmodels.api as sm 

#------------------------------------------------
# Black-Scholes Functions
#------------------------------------------------

def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate the Black-Scholes option price.

    Parameters:
    S : float : Current stock price
    K : float : Option strike price
    T : float : Time to expiration (in years)
    r : float : Risk-free interest rate (annualized)
    sigma : float : Volatility of the underlying stock (annualized)

    Returns:
    float : Black-Scholes option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = (S * sp.stats.norm.cdf(d1) - K * np.exp(-r * T) * sp.stats.norm.cdf(d2))
    return call_price

def black_scholes_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate the Black-Scholes put option price.

    Parameters:
    S : float : Current stock price
    K : float : Option strike price
    T : float : Time to expiration (in years)
    r : float : Risk-free interest rate (annualized)
    sigma : float : Volatility of the underlying stock (annualized)

    Returns:
    float : Black-Scholes put option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put_price = (K * np.exp(-r * T) * sp.stats.norm.cdf(-d2) - S * sp.stats.norm.cdf(-d1))
    return put_price

#------------------------------------------------
# Example Usage
#------------------------------------------------

if __name__ == "__main__":
    S = 100  # Current stock price
    K = 100  # Option strike price
    T = 1    # Time to expiration (1 year)
    r = 0.05 # Risk-free interest rate (5%)
    sigma = 0.2 # Volatility (20%)

    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    print(f"Call Price: {call_price}")
    print(f"Put Price: {put_price}")