"""
src/python/simulation_engine.py

Purpose: Is a central script that orchestrates the execution of the pricing models and risk analytics. It acts as the main runner or manager that calls functions from pricing_models and risk_analytics, potentially feeding them data prepared by data_loaders, and then processes or outputs the results.

Aim: To provide a streamlined and efficient workflow for running simulations, allowing for easy adjustments to parameters and quick access to results.
"""

# Importing pricing models
from pricing_models.binomial_tree import binomial_tree
from pricing_models.black_scholes import black_scholes_call, black_scholes_put
from pricing_models.monte_carlo_option import monte_carlo_simulation, plot_monte_carlo_simulation

# Import risk analytics
from risk_analytics.greek_calculator import Delta, Gamma, Vega, Theta, Rho

# Importing data_loaders
from data_loaders.market_data_api import fetch_raw_market_data, preprocess_market_data, calculate_technical_indicators

#---------------------------------------------------------
# Main Engine
#---------------------------------------------------------

def main():
    # Fetch raw market data
    raw_data = fetch_raw_market_data("AAPL", "2020-01-01", "2020-12-31", "yfinance")

    # Preprocess the data
    processed_data = preprocess_market_data(raw_data)

    # Calculate technical indicators
    final_data = calculate_technical_indicators(processed_data)

    # Find technical indicators
    rsi = final_data['RSI'].iloc[-1]
    macd = final_data['MACD'].iloc[-1]
    macd_signal = final_data['MACD_signal'].iloc[-1]

    print(f"RSI: {rsi}")
    print(f"MACD: {macd}")
    print(f"MACD Signal: {macd_signal}")

    # Run pricing models
    option_price = black_scholes_call(final_data, strike_price=150, risk_free_rate=0.01, time_to_maturity=30)
    print(f"Option Price (Black-Scholes Call): {option_price}")

    # Run risk analytics
    delta = Delta(final_data)
    gamma = Gamma(final_data)
    vega = Vega(final_data)
    theta = Theta(final_data)
    rho = Rho(final_data)

    print(f"Delta: {delta.calculate()}")
    print(f"Gamma: {gamma.calculate()}")
    print(f"Vega: {vega.calculate()}")
    print(f"Theta: {theta.calculate()}")
    print(f"Rho: {rho.calculate()}")

    # Display the final data
    print(final_data.head())

    # plot monte carlo sim
    plot_monte_carlo_simulation(final_data)

#-----------------------------------------------------------
# Example Usage
#-----------------------------------------------------------

if __name__ == "__main__":
    main()
