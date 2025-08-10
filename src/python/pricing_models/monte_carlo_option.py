"""
src/python/pricing_models/monte_carlo_option.py

Purpose: To implement the Monte Carlo simulation method for option pricing.

Aim: To provide a flexible and powerful tool for pricing a wide range of options, including exotic options.
"""
import pandas as pd 
import numpy as np 
import statsmodels.api as sm 
import matplotlib.pyplot as plt
import scipy as sp

#--------------------------------------------------------
# Monte Carlo Functions
#--------------------------------------------------------

def monte_carlo_simulation(S: float, K: float, T: float, r: float, sigma: float, num_simulations: int) -> float:
    """
    Perform Monte Carlo simulation to estimate the option price.

    Parameters:
    S : float : Current stock price
    K : float : Option strike price
    T : float : Time to expiration (in years)
    r : float : Risk-free interest rate (annualized)
    sigma : float : Volatility of the underlying stock (annualized)
    num_simulations : int : Number of simulation paths

    Returns:
    float : Estimated option price
    """
    # Simulate end stock prices
    dt = T / 365  # Daily steps
    num_steps = 365
    price_paths = np.zeros((num_steps, num_simulations))
    price_paths[0] = S

    for t in range(1, num_steps):
        z = np.random.normal(size=num_simulations)
        price_paths[t] = price_paths[t - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)

    # Calculate option payoffs
    call_payoffs = np.maximum(price_paths[-1] - K, 0)
    put_payoffs = np.maximum(K - price_paths[-1], 0)

    # Discount payoffs back to present value
    call_price = np.exp(-r * T) * np.mean(call_payoffs)
    put_price = np.exp(-r * T) * np.mean(put_payoffs)

    return call_price, put_price

def plot_monte_carlo_simulation(price_paths: np.ndarray, K: float) -> None:
    """
    Plot the Monte Carlo simulation paths and the option payoff.

    Parameters:
    price_paths : np.ndarray : Simulated price paths
    K : float : Option strike price
    """
    plt.figure(figsize=(12, 6))
    plt.plot(price_paths, lw=1)
    plt.axhline(y=K, color='r', linestyle='--', label='Strike Price')
    plt.title('Monte Carlo Simulation of Stock Price Paths')
    plt.xlabel('Time Steps')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

#-----------------------------------------------
# Example Usage
#-----------------------------------------------
if __name__ == "__main__":
    S = 100  # Current stock price
    K = 100  # Option strike price
    T = 1    # Time to expiration (in years)
    r = 0.05 # Risk-free interest rate (annualized)
    sigma = 0.2 # Volatility (annualized)
    num_simulations = 10000

    call_price, put_price = monte_carlo_simulation(S, K, T, r, sigma, num_simulations)
    print(f"Call Price: {call_price}")
    print(f"Put Price: {put_price}")

    plot_monte_carlo_simulation(price_paths, K)