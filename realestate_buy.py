import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

url = 'https://drive.google.com/file/d/1EPN31ajQi6j6OOFxq_g40jo3KWnas2l2/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)

st.header('**Realestate**')
st.subheader('YearWise Price Analysis')
select_date = st.selectbox('Select a date',df['date'].unique())
date = df[df['date'] == select_date]

price= date['price']
city = date['city']

price_year = px.bar( date,
    x= price,
    y= city,
    color='price' 
)
st.plotly_chart(price_year)



st.subheader('CityWise Price Analysis')
select_city = st.selectbox('Select a city',df['city'].unique())
city = df[df['city'] == select_city]


price= city['price']
year_of = city['date']


price_trend = px.line( city,
    x= price,
    y= year_of,
    color= 'city',
    markers=True
)

st.plotly_chart(price_trend)

st.subheader('Data listed for reference')

st.dataframe(city)

