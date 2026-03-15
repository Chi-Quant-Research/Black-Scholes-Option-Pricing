import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D
import os


# -----------------------------
# Black-Scholes Model
# -----------------------------

def d1(S,K,T,r,sigma):

    return (np.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))

def d2(S,K,T,r,sigma):

    return d1(S,K,T,r,sigma)-sigma*np.sqrt(T)


def call_price(S,K,T,r,sigma):

    return S*norm.cdf(d1(S,K,T,r,sigma))-K*np.exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))


def delta(S,K,T,r,sigma):

    return norm.cdf(d1(S,K,T,r,sigma))


def gamma(S,K,T,r,sigma):

    return norm.pdf(d1(S,K,T,r,sigma))/(S*sigma*np.sqrt(T))


def vega(S,K,T,r,sigma):

    return S*norm.pdf(d1(S,K,T,r,sigma))*np.sqrt(T)


def theta(S,K,T,r,sigma):

    term1=-(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*np.sqrt(T))
    term2=-r*K*np.exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
    return term1+term2


# -----------------------------
# Parameters
# -----------------------------

K=100
r=0.05
T=1

stock_prices=np.linspace(50,150,50)

vols=np.linspace(0.1,0.5,50)

S,V=np.meshgrid(stock_prices,vols)


# -----------------------------
# Compute Surfaces
# -----------------------------

price_surface=call_price(S,K,T,r,V)
delta_surface=delta(S,K,T,r,V)
gamma_surface=gamma(S,K,T,r,V)
vega_surface=vega(S,K,T,r,V)
theta_surface=theta(S,K,T,r,V)


# -----------------------------
# Create Results Folder
# -----------------------------

if not os.path.exists("results"):

    os.makedirs("results")


# -----------------------------
# 3D Plot Function
# -----------------------------

def plot_surface(X,Y,Z,title,filename):

    fig=plt.figure(figsize=(10,7))

    ax=fig.add_subplot(111,projection='3d')

    ax.plot_surface(X,Y,Z,cmap='viridis')

    ax.set_xlabel("Stock Price")

    ax.set_ylabel("Volatility")

    ax.set_zlabel(title)

    ax.set_title(title)

    plt.savefig("results/"+filename)

    plt.close()


# -----------------------------
# Generate Charts
# -----------------------------

plot_surface(S,V,price_surface,"Option Price","option_price_surface.png")

plot_surface(S,V,delta_surface,"Delta","delta_surface.png")

plot_surface(S,V,gamma_surface,"Gamma","gamma_surface.png")

plot_surface(S,V,vega_surface,"Vega","vega_surface.png")

plot_surface(S,V,theta_surface,"Theta","theta_surface.png")


print("All charts saved in results folder")