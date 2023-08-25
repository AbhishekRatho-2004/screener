import streamlit as st
from tradingview_screener import get_scanner_data, Scanner
import pandas as pd
from IPython.display import display,clear_output
import time as t
import plotly.graph_objects as go
import plotly.express as px
st.set_page_config(title='Screener',layout='wide')
st.header('Stock Screener')
st.subheader(':blue[PreMarket Gainer]')
st.write('''
What Is Pre-Market Trading?
Pre-market trading is the period of trading activity that occurs before the regular market session. The pre-market trading session typically occurs between 8 a.m. and 9:30 a.m. EST each trading day. Many investors and traders watch the pre-market trading activity to judge the strength and direction of the market in anticipation of the regular trading session.

Pre-market trading can only be executed with limited orders through an "electronic market" like an alternative trading system (ATS) or electronic communication network (ECN). Market makers are not permitted to execute orders until the 9:30 a.m. EST opening bell.
''')
df = Scanner.premarket_gainers.get_data()
st.table(df)
fig=px.bar(df,x='name',y='premarket_change',title='premarket Gainers premarket Change')
fig2=px.line(df,x='name',y='close',title='Closing price of the company by pre market gainers')
st.plotly_chart(fig2)
st.plotly_chart(fig,use_container_width=True)
st.subheader(':blue[PreMarket Most Active]')
st.write('''
Premarket most active in the stock market refers to the stocks or securities that have experienced the highest trading volumes during the premarket trading session. The premarket trading session is a period before the official market opening hours where traders and investors can place orders and trade securities.
When a stock is labeled as "premarket most active," it means that it has seen a significant amount of trading activity in terms of the number of shares being bought and sold during this premarket session.
''')
mostactive=Scanner.premarket_most_active.get_data()
st.table(mostactive.head(10))
fig3=px.bar(mostactive,x='name',y='premarket_volume',title='<h2>premarket Gainers premarket volume</h2>')
fig4=px.line(mostactive,x='name',y='close',title='Closing price of the company by pre market gainers')
st.plotly_chart(fig3,use_container_width=True)
st.plotly_chart(fig4,use_container_width=True)
st.subheader(':blue[Pre Market Loosers]')
st.write('''
Premarket losers in the stock market refers to those stocks or securities that have experienced a decrease in their prices during the premarket trading session. The premarket trading session is a period of trading that occurs before the official market opening hours. It allows traders and investors to place orders and react to news events that might have occurred outside of regular trading hours.
When a stock is labeled as a "premarket loser," it means that its price has declined during this premarket session compared to its closing price from the previous trading day. 
''')
premarketlossers=Scanner.premarket_losers.get_data(range=[0, 200])
st.table(premarketlossers.head(20))
fig5=px.bar(df,x='name',y='premarket_change',title='premarket loosers premarket Change')
fig6=px.line(df,x='name',y='close',title='Closing price of the company by pre market loosers')
st.plotly_chart(fig5)
st.plotly_chart(fig6,use_container_width=True)
