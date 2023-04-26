from flask import Flask, render_template, request, jsonify, url_for, redirect
import requests
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    symbol = None
    current_price = None
    threshold = None
    message = None
    if request.method == 'POST':
        symbol = request.form['symbol']
        threshold_input = request.form.get('threshold')
        if threshold_input:
            threshold = float(threshold_input)
        else:
         threshold = None

        # stock = yf.Ticker("ABEV3.SA")
        # price = stock.info['regularMarketPrice']
        # print(price)
        tickerSymbol =  symbol

        tickerData = yf.Ticker(tickerSymbol)
        todayData = tickerData.history(period='1d')
        x = todayData['Close'][0]
        

        current_price = x # This is just an example.
        print(x)
        print(threshold)
        if current_price >= threshold:
            message = f"The current price of {symbol} is {current_price:.2f}. It has reached your threshold of {threshold:.2f}."
            
        else:
            message = f"The current price of {symbol} is {current_price:.2f}. It has not reached your threshold of {threshold:.2f}."
        print(message)
    return render_template('index.html', message = message)



@app.route('/result')
def price():
    return render_template('result.html')
    # return redirect(url_for('https:/finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC'))


if __name__ == '__main__':
    app.run(debug=True)
