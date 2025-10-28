import yfinance as yf
import numpy as np
import pandas as pd

def analyze_portfolio(tickers, allocations):
    weights = np.array(allocations) / np.sum(allocations)
    data = yf.download(tickers, period='1y')['Close']
    daily_returns = data.pct_change().dropna()

    portfolio_returns = (daily_returns * weights).sum(axis=1)
    trading_days = len(portfolio_returns)
    annual_return = (1 + np.mean(portfolio_returns)) ** trading_days - 1
    volatility = np.std(portfolio_returns) * np.sqrt(trading_days)

    risk_free_rate = 0.065
    sharpe_ratio = (annual_return - risk_free_rate) / volatility

    correlation_matrix = daily_returns.corr().round(2).to_dict()

    return {
        "annualizedReturn": round(annual_return * 100, 2),
        "volatility": round(volatility * 100, 2),
        "sharpeRatio": round(sharpe_ratio, 2),
        "correlationMatrix": correlation_matrix
    }
