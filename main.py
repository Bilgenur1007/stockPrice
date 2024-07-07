import streamlit as st
import yfinance as yf
import pandas as pd

st.write(
    """
    # Simple Stock Price App
    
    Shown are the stock **closing pricing** and ***volume*** of Google

    
    """
)

#define the ticker symbol
tickerSymbol="AAPL"
#AAPL for apple
#get data on this timer
tickerData=yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf=tickerData.history(period="1d",start="2010-01-01",end="2020-01-01")
#Open High Low Close Valume Dividends Start

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

