import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'TSLA'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2012-12-25', end='2022-12-25')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
#get recommendation data for ticker
tickerData.recommendations
#info on the company
tickerData.info

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
