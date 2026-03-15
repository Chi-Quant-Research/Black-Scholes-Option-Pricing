# Black–Scholes Quantitative Research (Python)

## Overview

This repository implements the Black–Scholes option pricing framework and visualizes option sensitivities using 3D surfaces.

The project demonstrates core techniques used in derivatives pricing, volatility modeling, and financial risk management.

It includes visualization of option price behavior and the Greeks across different market conditions.

---

# Quantitative Finance Context

The Black–Scholes model is a fundamental framework used in quantitative finance to price European options and analyze derivatives risk.

Understanding the behavior of option prices and Greeks is essential for:

• derivatives trading
• volatility modeling
• portfolio hedging
• financial risk management

---

# Model Inputs

Underlying price range: 50 – 150
Strike price: 100
Volatility range: 10% – 50%
Risk-free rate: 5%
Time to maturity: 1 year

---

# Key Results

The project produces 3D surfaces that illustrate how option values and sensitivities change across different market conditions.

Visualizations include:

• Option Price Surface
• Delta Surface
• Gamma Surface
• Vega Surface
• Theta Surface

---

# Results

## Option Price Surface

![Option Price](results/option_price_surface.png)

## Delta Surface

![Delta](results/delta_surface.png)

## Gamma Surface

![Gamma](results/gamma_surface.png)

## Vega Surface

![Vega](results/vega_surface.png)

## Theta Surface

![Theta](results/theta_surface.png)

---

# Repository Structure

black-scholes-quant-research

README.md
requirements.txt
black_scholes_quant_research.py

results/
option_price_surface.png
delta_surface.png
gamma_surface.png
vega_surface.png
theta_surface.png

---

# How to Run

Install dependencies

pip install -r requirements.txt

Run the simulation

python black_scholes_quant_research.py

All charts will be generated automatically inside the results folder.

---

# Key Takeaways

This project demonstrates:

• derivatives pricing using the Black–Scholes framework
• sensitivity analysis through option Greeks
• 3D visualization of financial models
• quantitative modeling using Python

These techniques are widely used in quantitative research and derivatives trading.

---

# Technologies

Python
NumPy
SciPy
Matplotlib
