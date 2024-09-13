#importing necessary libararies
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression.linear_model import OLS


tickers = ['AAPL', 'MSFT', 'TSLA', 'JNJ', 'V', 'AMZN', 'WMT', 'KO', 'PFE', 'NFLX']

cointegrated_pairs = []

def fetch_data(tickers, startdate, enddate):
    data = yf.download(tickers, start = startdate, end = enddate)['Adj Close']
    data = data.dropna()

    return data



def engle_granger_two_step_coint_test(stock1, stock2):


    
    result = OLS(stock1, stock2).fit()
    residuals = result.residuals
    adf = adfuller(residuals)



    print(f"---regression result---\n\nr-value: {result.rvalue}\np-value: {result.pvalue}\n\n ---Augmented Dickey Fuller test result---\n\n test stat: {adf[0]}\n critical value: {adf[4]['5%']}")

    return adf[2]



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

    print(data.residuals)
    




