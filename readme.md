# Goals

the purpose of this repo is to explore the mathematics and ideas behind pair trading in python.

specifically we explore statistical tests that give insights into the relationships found in time series data.

the goals are but not limited to...
1. Gain experience working with time series data. (graphing, data-cleaning, mathematics with dataframes etc)
2. Apply the Granger Causality Test and understand and interpret the underlying math as well as the output
3. Test for Cointegration using the Augmented Dickey-Fuller Test and understand it to the same degree as the Granger Causality Test
4. Apply the above tests to different data points to explore the different variables at play
5. What next steps are possible given this new SUPREME POWER!!

# Key Def

## Lag
- in our case lag is the number of previous observations used to predict the current value

## Stationary Time Series
- a stationary time series implies two things: 

1. Mean Reversion: The difference between the two stock prices tends to revert to a stable mean. If the spread deviates from this mean, it is likely to move back toward it over time.

2. Constant Variability: The variability in the delta remains consistent over time, indicating no increasing or decreasing trend in the spread's volatility.


# Granger Causality Test

- In our code we create a matrix that tests the Granger Causality for all combinations i.e NTFLX and META 
- the arguemnts are self explantory but test specifies which statistical test to use
- For each combination of possible causality the function tests whether the lags of one variable Granger cause-the other
- It returns the minimum p-value from the lags and can be compared to significane level to reject the null hypthosis that **X does not Granger-Cause Y**
- In summary the test focuses on the short term predictive relationships however it does not account for long-term relationships
- Be wary that the test is misleading for time series pairs that are not stationary
- This is where the Engle Granger Test comes in hand 


# Cointegration Test(Engle Granger OR Johansen tests)

- we first check the residuals for cointegration after fitting the variables to a linear relationship

- the Augmented Dickey-Fueller test is related to the Cointegration test 

- the Engle Granger test uses the ADF test to check if the residulas are stationary and if so then we arrive at the conclusion that the stocks are cointegrated




## Augmented Dickey-Fuller Test
- a statistical test in time series analysis to determine whether a given time seires is stationary or contains a unit root(implies non-stationary)

- Our null hypthosis is that the time series is non-stationary
- the test calculates a test statistic based on the lagged differences of the time series
- we compare the test statistic to critical values derived from the Dickey-Fuller distribution
- there are common criteria that determine the number of lags like
    - Akaike Information Criterion
    - Bayesian Information Criterion
- if the ADF suggests non-stationarity we may need to subtract the previous observation from the current one


# Next Steps

- Now that we understand that NFLX and META are cointegrated we can analyze the spread(NFLX - META)
- using the ADF test we check for the stationarity of the spread and take the implications of the result and look to profit 

- in our code we check the stationarity of the spread(NFLX - META) and conclude it is stationary 
- combining mean reversion and constant variability we can create a pairs strategy 

# Pairs Trading 
- there are 3 steps we must follow to develop a strategy
1. Define the Trading Spread
    - This involves defining a function of time 
    - Spread(t) = META(t) - B * NFLX(t)
    - where B is the hedge ratio typcially estimate by regressing METa on NFLX
2. Identify the Mean of the Spread
    - calculate the mean of the spread using historical data
    - this serves as the benchmark for determining when the spread has deviated significantly and is likely to revert

3. Establish Entry and Exit Signals
    - Entry Points:
        - **Long Spread(Buy META, Sell NFLX)**: enter a long position when the spread deviates below a threshold(i.e mean -2 sd)
        - **Short Spread(Sell META, Buy NFLX)**: enter a short position when the spread deviates above a threshold(i.e mean +2 sd)
    - Exit Points:
        - close the position when the spread reverts to the mean
        - or crosses a predefined level
        - i.e within 1 standard deviation of the mean
        