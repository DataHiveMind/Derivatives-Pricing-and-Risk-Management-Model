"""
src/python/risk_analytics/greek_calculator.py

Purpose: Contains functions to compute the "Greeks"- Delta, Gamma, Vega, Theta, and Rho. These measures quantify an option's sensitivity to changes in the underlying asset's price, volatility, time to expiration, and interest rates, respectively.

Aim: To provide a comprehensive set of tools for risk management and derivatives pricing by computing the Greeks for various options.
"""

import pyqaunt
import arch 
import quantlib
import py_vollib

#-----------------------------------------------------------------------------
# Greek Calculator Functions
#------------------------------------------------------------------------------

def Delta(option: str, underlying_price: float, 
    volatility: float, time_to_expiration: float, risk_free_rate: float) -> float:
    """
    Purpose: Computes the Delta of a European option using the Black-Scholes model.

    Parameters:
    option: The type of the option (e.g., 'call' or 'put') 
    underlying_price: The current price of the underlying asset
    volatility: The volatility of the underlying asset
    time_to_expiration: The time to expiration of the option (in years)
    risk_free_rate: The risk-free interest rate (annualized)

    Returns:
    The Delta of the option (sensitivity to changes in the underlying asset's price)
    """
    return py_vollib.black_scholes.greeks.delta(option, underlying_price, volatility, time_to_expiration, risk_free_rate)

def Gamma(option: str, underlying_price: float, 
    volatility: float, time_to_expiration: float, risk_free_rate: float) -> float:
    """
    Purpose: Computes the Gamma of a European option using the Black-Scholes model.

    Parameters:
    option: The type of the option (e.g., 'call' or 'put') 
    underlying_price: The current price of the underlying asset
    volatility: The volatility of the underlying asset
    time_to_expiration: The time to expiration of the option (in years)
    risk_free_rate: The risk-free interest rate (annualized)

    Returns:
    The Gamma of the option (sensitivity to changes in Delta)
    """
    return py_vollib.black_scholes.greeks.gamma(option, underlying_price, volatility, time_to_expiration, risk_free_rate)

def Vega(option: str, underlying_price: float, 
    volatility: float, time_to_expiration: float, risk_free_rate: float) -> float:
    """
    Purpose: Computes the Vega of a European option using the Black-Scholes model.

    Parameters:
    option: The type of the option (e.g., 'call' or 'put') 
    underlying_price: The current price of the underlying asset
    volatility: The volatility of the underlying asset
    time_to_expiration: The time to expiration of the option (in years)
    risk_free_rate: The risk-free interest rate (annualized)

    Returns:
    The Vega of the option (sensitivity to volatility changes)
    """
    return py_vollib.black_scholes.greeks.vega(option, underlying_price, volatility, time_to_expiration, risk_free_rate)

def Theta(option: str, 
    underlying_price: float, volatility: float, 
    time_to_expiration: float, risk_free_rate: float) -> float:
    """
    Purpose: Computes the Theta of a European option using the Black-Scholes model.

    Parameters:
    option: The type of the option (e.g., 'call' or 'put') 
    underlying_price: The current price of the underlying asset
    volatility: The volatility of the underlying asset
    time_to_expiration: The time to expiration of the option (in years)
    risk_free_rate: The risk-free interest rate (annualized)

    Returns:
    The Theta of the option (sensitivity to time decay)
    """
    return py_vollib.black_scholes.greeks.theta(option, underlying_price, volatility, time_to_expiration, risk_free_rate)

def Rho(option: str, underlying_price: float, 
    volatility: float, time_to_expiration: float, risk_free_rate: float) -> float:
    """
    Purpose: Computes the Rho of a European option using the Black-Scholes model.

    Parameters:

    option: The type of the option (e.g., 'call' or 'put') 
    underlying_price: The current price of the underlying asset
    volatility: The volatility of the underlying asset
    time_to_expiration: The time to expiration of the option (in years)
    risk_free_rate: The risk-free interest rate (annualized)

    Returns:
    The Rho of the option (sensitivity to interest rate changes)
    """
    return py_vollib.black_scholes.greeks.rho(option, underlying_price, volatility, time_to_expiration, risk_free_rate)

    #---------------------------------------------------------------
    # Example Usage
    #---------------------------------------------------------------
    if __name__ == "__main__":
        option = 'call'
        underlying_price = 100
        volatility = 0.2
        time_to_expiration = 1
        risk_free_rate = 0.05

        print("Delta:", Delta(option, underlying_price, volatility, time_to_expiration, risk_free_rate))
        print("Gamma:", Gamma(option, underlying_price, volatility, time_to_expiration, risk_free_rate))
        print("Vega:", Vega(option, underlying_price, volatility, time_to_expiration, risk_free_rate))
        print("Theta:", Theta(option, underlying_price, volatility, time_to_expiration, risk_free_rate))
        print("Rho:", Rho(option, underlying_price, volatility, time_to_expiration, risk_free_rate))