# import streamlit as st
# import plotly.graph_objs as go
# import yfinance as yf
# from datetime import datetime
# from datetime import date
# import pandas as pd

# # create a Streamlit app
# st.title('Real-time Candlestick Chart')

# # define a function to generate a candlestick chart
# def candlestick_chart(df):
#     fig = go.Figure(data=[go.Candlestick(x=df.index,
#                                          open=df['Open'],
#                                          high=df['High'],
#                                          low=df['Low'],
#                                          close=df['Close'])])

#     fig.update_layout(title='Candlestick Chart',
#                       xaxis_title='Datetime',
#                       yaxis_title='Price')

#     return fig

# # load the initial data for the chart
# # ticker = 'AAPL'
# # start_date ="2015-01-01" #datetime.now().strftime('%Y-%m-%d')
# # end_date = datetime.now().strftime('%Y-%m-%d')
# START = datetime.now().strftime('%Y-%m-%d')#"2015-01-01"
# TODAY = date.today().strftime("%Y-%m-%d")

# url = 'https://drive.google.com/file/d/1QK5XmrztKAUM4Pu3Fy2dbKPFwhUuJDa9/view?usp=share_link'
# path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]



# stocks =  pd.read_csv(path)
# selected_stock = st.selectbox("Select dataset for prediction", stocks)
# @st.cache_data
# def load_data(ticker):
#     data = yf.download(ticker, START, TODAY)
#     data.reset_index(inplace = True)
#     return data

# # data_load_state = st.text("Load data...")
# data = load_data(selected_stock)
# data1 = yf.download(data, start=START, end=TODAY, interval='1m')
# chart_fig = candlestick_chart(data1)


# # display the chart in Streamlit
# st.plotly_chart(chart_fig)

# # create a connection to a real-time data source (e.g., a websocket)
# # and continuously update the chart with new data
# while True:
#     new_data = yf.download(data, start=START, end=TODAY, interval='1m')
#     data1 = data.append(new_data)
#     chart_fig = candlestick_chart(data1)
#     st.plotly_chart(chart_fig)
import streamlit as st
import plotly.graph_objs as go
import yfinance as yf
from datetime import datetime

# create a Streamlit app
st.title('Real-time Candlestick Chart')

# define a function to generate a candlestick chart
def candlestick_chart(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])

    fig.update_layout(title='Candlestick Chart',
                      xaxis_title='Datetime',
                      yaxis_title='Price')

    return fig

# load the initial data for the chart
ticker = 'AAPL'
start_date = datetime.now().strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')
data = yf.download(ticker, start=start_date, end=end_date, interval='1m')
chart_fig = candlestick_chart(data)

# display the chart in Streamlit
st.plotly_chart(chart_fig)

# create a connection to a real-time data source (e.g., a websocket)
# and continuously update the chart with new data
while True:
    new_data = yf.download(ticker, start=start_date, end=end_date, interval='1m')
    data = data.append(new_data)
    chart_fig = candlestick_chart(data)
    st.plotly_chart(chart_fig)