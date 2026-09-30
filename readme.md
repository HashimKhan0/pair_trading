# Pairs Trading: Cointegration & Granger Causality

Exploring the statistics behind **pairs trading** in Python: finding stock pairs whose prices move together over the long run, testing whether their spread is mean-reverting, and turning that spread into entry/exit signals.

## Goals

1. Get hands-on with financial time series: downloading, cleaning, plotting and doing math on price DataFrames.
2. Apply the **Granger causality test** and interpret both the math and the output.
3. Test for **cointegration** with the Engle–Granger two-step method (OLS + Augmented Dickey–Fuller on the residuals).
4. Screen many tickers for cointegrated pairs.
5. Turn a cointegrated pair into a mean-reversion trading rule.

## Method

**1. Granger causality.** For every ticker pair, test whether lags of one series help predict the other and keep the minimum p-value across lags (H₀: *X does not Granger-cause Y*). This captures short-term predictive relationships but is unreliable on non-stationary series — hence step 2.

**2. Cointegration (Engle–Granger).** Regress one price on the other and run an ADF test on the residuals (H₀: unit root / non-stationary). Stationary residuals imply the pair is cointegrated. NFLX and META are cointegrated in the sample studied.

**3. The spread.**

$$\text{Spread}_t = \text{META}_t - \beta \cdot \text{NFLX}_t$$

where β, the hedge ratio, is estimated by regressing META on NFLX. The spread is checked for stationarity (mean reversion + constant variance).

**4. Signals.**

| Condition | Action |
|---|---|
| Spread < mean − 2σ | **Long the spread**: buy META, sell NFLX |
| Spread > mean + 2σ | **Short the spread**: sell META, buy NFLX |
| Spread returns to within 1σ of the mean | Close the position |

## Repository layout

```
cointegration.ipynb   # Granger-causality matrix, Engle–Granger test, spread analysis (NFLX / META)
S&P_500.ipynb         # extending the search to S&P 500 constituents
main.py               # two-ticker pipeline: fetch, plot, cointegration test, spread
test.py               # screen a basket (AAPL, MSFT, TSLA, JNJ, V, AMZN, WMT, KO, PFE, NFLX) for cointegrated pairs
```

## Running it

```bash
pip install pandas numpy yfinance matplotlib statsmodels
python main.py
```

## Key definitions

- **Lag:** number of past observations used to predict the current value.
- **Stationarity:** constant mean and variance over time; for a spread, this means deviations tend to revert.
- **ADF test:** tests for a unit root; lag length can be chosen by AIC/BIC. If a series is non-stationary, differencing is the usual fix.

## Tech stack

Python · pandas · NumPy · statsmodels · yfinance · matplotlib
