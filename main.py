#importing necessary libararies
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.stattools import adfuller
from scipy.stats import linregress

def fetch_data(ticker1, ticker2, startdate, enddate):
    data = yf.download([ticker1, ticker2], start = startdate, end = enddate)['Adj Close']
    data = data.dropna()

    return data

def plot_data(data,ticker1,ticker2):
    data[ticker1].plot(figsize = (10, 5), label = ticker1, color = 'blue')
    data[ticker2].plot(figsize = (10, 5), label = ticker2, color = 'red')
    plt.legend()
    plt.show()



def engle_granger_two_step_coint_test(data):
    
    result = linregress(data[ticker1], data[ticker2])
    predict = result.slope * data[ticker1] + result.intercept
    residuals = data[ticker2] - predict
    adf = adfuller(residuals)

    print(f"---regression result---\n\nr-value: {result.rvalue}\np-value: {result.pvalue}\n\n ---Augmented Dickey Fuller test result---\n\n test stat: {adf[0]}\n critical value: {adf[4]['5%']}")


def 
    

if __name__ == '__main__':
    ticker1 = input("Enter the first ticker").upper()
    ticker2 = input("Enter the second ticker").upper()

    startdate = input("Enter the start date(YYYY-MM-DD)")
    enddate = input("Enter the end date(YYYY-MM-DD)")

    data = fetch_data(ticker1, ticker2, startdate, enddate)

    plot_data(data,ticker1,ticker2)

    engle_granger_two_step_coint_test(data)





