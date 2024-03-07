import streamlit as st 
from datetime import date

import pandas as pd 
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

def show_oil():    
    START = "04-01-2000"
    END = "01-09-2022"

    st.title("Crude Price Prediction")

    url = 'https://drive.google.com/file/d/1e9_Vj15vSOKpU9qGrWXJBnow_t3ZyEod/view?usp=sharing'
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    data = pd.read_csv(path)
    data.head()

    st.subheader('Raw data')
    st.write(data.head(100))

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close/Last'], name='crude_close'))
        fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()


    df_train = data[['Date','Close/Last']]
    df_train = df_train.rename(columns={"Date": "ds", "Close/Last": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)


    st.subheader('Forecast data')
    st.write(forecast.tail())

    st.write('forecast data')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.write('forecast components')
    fig2 = m.plot_components(forecast)
    st.write(fig2)