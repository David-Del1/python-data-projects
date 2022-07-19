import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock price app. This is (stream) lit!

""")

# Define the ticker symbol
tickerSymbol = 'NFLX'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get the historical price for this ticker
tickerDF = tickerData.history(period='1d', start='2002-7-17', end='2022-7-17')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
