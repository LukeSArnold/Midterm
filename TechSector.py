import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def part1():
    # open up both csvs as a pandas dataframe
    apple_frame = pd.read_csv("csvs/AAPL.csv")
    tesla_frame = pd.read_csv("csvs/TSLA.csv")

    dates = apple_frame['Date'].to_numpy().tolist()
    apple_stock = apple_frame['Close'].to_numpy().tolist()
    tesla_stock = tesla_frame['Close'].to_numpy().tolist()

    for i in range(len(apple_stock)):
        apple_stock[i] = float(apple_stock[i].replace('$',''))
        
    apple_stock.reverse()
    tesla_stock.reverse()
    dates.reverse()
    
    # plotting closing stock prices
    plt.plot(dates, apple_stock, label='Apple Stock')
    plt.plot(dates, tesla_stock, label='Tesla Stock')
    plt.legend()
    plt.title('Apple vs Tesla Closing Stock Prices')
    plt.xticks(np.arange(0, len(apple_stock), 150), fontsize=5)
    plt.show()

    # plotting difference between high and low prices 
    apple_difference = []
    apple_high = apple_frame[' High'].to_numpy().tolist()
    apple_low = apple_frame[' Low'].to_numpy().tolist()

    for i in range(len(apple_high)):
        apple_high[i] = float(apple_high[i].replace('$',''))
        apple_low[i] = float(apple_low[i].replace('$',''))
        apple_difference.append(apple_high[i] - apple_low[i])

    tesla_difference = []
    tesla_high = tesla_frame['High'].to_numpy().tolist()
    tesla_low = tesla_frame['Low'].to_numpy().tolist()

    for i in range(len(tesla_high)):
        tesla_difference.append(tesla_high[i] - tesla_low[i])

    apple_difference.reverse()
    sns.displot(apple_difference, kde=True).set(title='Apple Stock Prices, Distribution of High Low Difference')
    plt.show()

    tesla_difference.reverse()
    sns.displot(tesla_difference, kde=True).set(title='Tesla Stock Prices, Distribution of High Low Difference')
    plt.show()
    
    sns.displot(apple_stock, kde=True).set(title='Apple Stock Prices, Distribution of Closing Price')
    plt.show()

    sns.displot(tesla_stock, kde=True).set(title='Tesla Stock Prices, Distribution of Closing Price')
    plt.show()

def part2():

    class European_Call_Payoff:

        def __init__(self, strike):
            self.strike = strike
        def get_payoff(self, stock_price):
            if stock_price > self.strike:
                return stock_price - self.strike
            else:
                return 0

    class GeometricBrownianMotion:

        def simulate_paths(self):
            while(self.T - self.dt > 0):
                dWt = np.random.normal(0, math.sqrt(self.volatility))  # Brownian motion
                dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
                self.current_price += dYt  # Add the change to the current price
                self.prices.append(self.current_price)  # Append new price to series
                self.T -= self.dt  # Account for the step in time

        def __init__(self, initial_price, drift, volatility, dt, T):
            self.current_price = initial_price
            self.initial_price = initial_price
            self.drift = drift
            self.volatility = volatility
            self.dt = dt
            self.T = T
            self.prices = []
            self.simulate_paths()

    

if __name__ == '__main__':
    if 'part1' in sys.argv:
        part1()
    elif 'part2' in sys.argv:
        part2()
