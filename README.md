# Black–Scholes Option Pricing Model (Python)

## Overview

This repository implements the Black–Scholes option pricing model using Python.

The project demonstrates quantitative techniques used in derivatives pricing and financial risk modeling. The model calculates European call option prices and visualizes how option values change with the underlying asset price.

The implementation also includes option sensitivity measures known as the Greeks.

---

# Quantitative Finance Context

The Black–Scholes framework is one of the most widely used models in quantitative finance.

It is commonly applied in:

• derivatives pricing
• volatility analysis
• financial risk management
• options trading

Understanding option price dynamics is essential for quantitative researchers and derivatives traders.

---

# Model

The price of a European call option under the Black–Scholes model is:

C = S N(d1) − K e^(−rT) N(d2)

Where

S = underlying asset price
K = strike price
T = time to maturity
r = risk-free interest rate
σ = volatility

The model also produces the option Greeks which measure sensitivity to different risk factors.

---

# Dataset

This project uses simulated asset prices to analyze option price behavior.

Simulation parameters:

Underlying price range: 50 – 150
Strike price: 100
Volatility: 20%
Risk-free rate: 5%
Time to maturity: 1 year

---

# Key Results

The model generates an option pricing curve that shows the nonlinear relationship between the underlying asset price and the option value.

Key observations:

• option price increases with underlying price
• convex payoff structure typical of options
• higher volatility increases option value

---

# Output

The simulation produces the following output:

results/option_price_curve.png

The chart illustrates how the call option price varies with the underlying stock price.

---

# Chart Result

Option Price

|
|        /
|      /
|    /
|  /
|/
+----------------------
Stock Price

---

# Repository Structure

black-scholes-option-pricing

data/
results/
black_scholes_option_pricing.py
requirements.txt
README.md

---

# How to Run

Step 1 – Install dependencies

pip install -r requirements.txt

Step 2 – Run the model

python black_scholes_option_pricing.py

Step 3 – View the generated chart

results/option_price_curve.png

---

# Key Takeaways

This project demonstrates:

• implementation of option pricing models
• quantitative modeling using Python
• financial risk sensitivity analysis
• visualization of derivatives pricing behavior

These techniques are widely used in quantitative research and derivatives trading.

---

# Technologies

Python
NumPy
SciPy
Matplotlib
