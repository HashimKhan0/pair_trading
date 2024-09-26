#importing necessary libararies
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression.linear_model import OLS

def fetch_data(ticker1, ticker2, startdate, enddate):
    data = yf.download([ticker1, ticker2], start = startdate, end = enddate)['Adj Close']
    data = data.dropna()

    return data

def plot_data(data,ticker1,ticker2):
    data[ticker1].plot(figsize = (10, 5), label = ticker1, color = 'blue')
    data[ticker2].plot(figsize = (10, 5), label = ticker2, color = 'red')
    plt.title(f"Adjust closing price of {ticker1} & {ticker2}")
    plt.legend()
    plt.show()



def engle_granger_two_step_coint_test(data):
    
    result = OLS(data[ticker1], data[ticker2]).fit()
    residuals = result.resid
    
    adf = adfuller(residuals)

    print(f"---Augmented Dickey Fuller test result---\n\n test stat: {adf[0]}\n critical value: {adf[4]['5%']}")


def create_spread(data):

    data['Spread'] = data[ticker1] - data[ticker2]



def plot_spread(data, ticker1, ticker2):
    plt.plot(data.index, data.Spread)

    avg_spread = data['Spread'].mean()

    plt.axhline(y=avg_spread, color='red', linestyle='--', linewidth=2)

    plt.subplots_adjust(left=4, right=10, top=0.9, bottom=0.1)

    plt.ylabel('Spread')
    plt.legend()





if __name__ == '__main__':
    ticker1 = input("Enter the first ticker: ").upper()
    ticker2 = input("Enter the second ticker: ").upper()

    startdate = input("Enter the start date(YYYY-MM-DD): ")
    enddate = input("Enter the end date(YYYY-MM-DD): ")

    data = fetch_data(ticker1, ticker2, startdate, enddate)
    
    engle_granger_two_step_coint_test(data)

    create_spread(data)

    plot_spread(data, ticker1, ticker2)