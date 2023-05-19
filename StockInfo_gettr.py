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

# Define the file path with the correct file name and extension
file_path = r"C:\Users\Mitchell\Desktop\learnding C\FinTools.txt"

# Convert the dividend value to a string
text = str(latest_dividend_value)

# Write the text to the file
with open(file_path, 'w') as file:
    file.write(text)
