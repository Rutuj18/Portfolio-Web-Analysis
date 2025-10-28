import yfinance as yf
import numpy as np
import pandas as pd

def analyze_portfolio(tickers, allocations):
    weights = np.array(allocations) / np.sum(allocations)
    data = yf.download(tickers, period='1y')['Close']
    daily_returns = data.pct_change().dropna()

    portfolio_returns = (daily_returns * weights).sum(axis=1)

    annual_return = np.mean(portfolio_returns) * 250
    volatility = np.std(portfolio_returns) * np.sqrt(250)
    risk_free_rate = 0.05
    sharpe_ratio = (annual_return - risk_free_rate) / volatility

    cumulative_return = (1 + portfolio_returns).cumprod()
    rolling_max = cumulative_return.cummax()
    drawdown = cumulative_return / rolling_max - 1
    max_drawdown = drawdown.min()

    correlation_matrix = daily_returns.corr().round(2).to_dict()

    return {
        "annualizedReturn": round(annual_return * 100, 2),
        "volatility": round(volatility * 100, 2),
        "sharpeRatio": round(sharpe_ratio, 2),
        "maxDrawdown": round(max_drawdown * 100, 2),
        "correlationMatrix": correlation_matrix
    }
