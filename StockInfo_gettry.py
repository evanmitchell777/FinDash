import yfinance as yf
import csv

def process_data(ticker):
    # Download stock data from yfinance
    stock = yf.Ticker(ticker)
    history = stock.history(period="max")

    # Calculate the response column
    rows = []
    for i in range(len(history)-1):
        today_close = history.iloc[i]['Close']
        tomorrow_close = history.iloc[i+1]['Close']
        if tomorrow_close > today_close:
            response = 'buy'
        else:
            response = 'sell'
        rows.append([history.index[i].strftime("%Y-%m-%d"), today_close, history.iloc[i]['Open'], history.iloc[i]['High'], history.iloc[i]['Low'], response])
    rows.append([history.index[-1].strftime("%Y-%m-%d"), history.iloc[-1]['Close'], history.iloc[-1]['Open'], history.iloc[-1]['High'], history.iloc[-1]['Low'], ''])

    # Write the data to a csv file
    with open(f'{ticker}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Close', 'Open', 'High', 'Low', 'Response'])
        writer.writerows(rows)

if __name__ == '__main__':
    ticker = input('Enter stock ticker symbol: ')
    process_data(ticker)
