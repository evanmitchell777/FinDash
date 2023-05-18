#To do: Make it to where data is stored somewhere in memory (text file csv etc.) 
import yfinance as yf

fund_name = input("Enter the ticker symbol of the mutual fund: ")

# Create a Ticker object
fund = yf.Ticker(fund_name)

# Gathers YTD performance
YTD = fund.history(period="YTD")['Close'].pct_change()[-1] * 100

# Gathers one-year performance
one_year_performance = fund.history(period="1y")['Close'].pct_change()[-1] * 100

# Gathers three-year performance
three_year_performance = fund.history(period="3y")['Close'].pct_change()[-1] * 100

# Gathers five-year performance
five_year_performance = fund.history(period="5y")['Close'].pct_change()[-1] * 100

# Gathers ten-year performance
ten_year_performance = fund.history(period="10y")['Close'].pct_change()[-1] * 100

# Get the dividend info
dividends = fund.dividends
latest_dividend_value = dividends[-1]
print(latest_dividend_value)
