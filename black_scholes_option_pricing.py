import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os


# ----------------------------
# Black-Scholes Pricing Model
# ----------------------------

def black_scholes_call(S, K, T, r, sigma):

    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

    d2 = d1 - sigma * np.sqrt(T)

    call_price = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

    return call_price


# ----------------------------
# Simulation Parameters
# ----------------------------

strike_price = 100
risk_free_rate = 0.05
volatility = 0.2
time_to_maturity = 1

stock_prices = np.linspace(50,150,100)

option_prices = []


# ----------------------------
# Calculate Option Prices
# ----------------------------

for S in stock_prices:

    price = black_scholes_call(
        S,
        strike_price,
        time_to_maturity,
        risk_free_rate,
        volatility
    )

    option_prices.append(price)


# ----------------------------
# Create Results Folder
# ----------------------------

if not os.path.exists("results"):
    os.makedirs("results")


# ----------------------------
# Plot Results
# ----------------------------

plt.figure(figsize=(8,5))

plt.plot(stock_prices, option_prices)

plt.title("Black-Scholes Call Option Price")

plt.xlabel("Stock Price")

plt.ylabel("Option Price")

plt.grid(True)

plt.savefig("results/option_price_curve.png")

plt.show()


print("Option pricing chart saved in results/option_price_curve.png")