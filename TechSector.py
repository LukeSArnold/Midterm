import sys
import pandas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def part1():
    # open up both csvs as a pandas dataframe
    apple_frame = pd.read_csv("csvs/AAPL.csv")
    tesla_frame = pd.read_csv("csvs/TSLA.csv")

    dates = apple_frame['Date'].to_numpy().tolist()
    apple_stock = apple_frame['Close'].to_numpy().tolist()
    tesla_stock = tesla_frame['Close'].to_numpy().tolist()

    print(tesla_stock[:50])
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

    plt.figure()

    # plotting difference between high and low prices 
    apple_difference = []
    apple_high = apple_frame['High'].to_numpy().tolist()
    apple_low = apple_frame['Low'].to_numpy().tolist()

    for i in range(len(apple_high)):
        apple_high[i] = float(apple_high[i].replace('S',''))
        apple_difference.append(apple_high[i] - apple_low[i])

    tesla_difference = []
    tesla_high = tesla_frame['High'].to_numpy().tolist()
    tesla_low = tesla_frame['Low'].to_numpy().tolist()

    for i in range(len(tesla_high)):
        tesla_difference.append(tesla_high - tesla_low)

    plt.title("Apple vs Tesla, Difference between High and Low Prices")
    plt.plot(dates, apple_difference, label = 'Apple')
    plt.plot(dates, tesla_difference, label = 'Tesla')
    plt.legend()
    plt.show()
    

if __name__ == '__main__':
    if 'part1' in sys.argv:
        part1()
