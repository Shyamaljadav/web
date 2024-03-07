import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

url = 'https://drive.google.com/file/d/14Gw_cQz_FnInMiolhkDjEAcjGzgL35ZC/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)


st.header('Real Estate')

st.subheader('Citywise Rent')
select_city = st.selectbox('Select a city',df['city'].unique())
city = df[df['city'] == select_city]
price= city['price']
area= city['area']
seller_type= city['seller_type']
property_type = city['property_type']
bedroom= city['bedroom']
bathroom= city['bathroom']
furnish_type= city['furnish_type']
locality= city['locality']


st.subheader('Price trend of the city')
price_trend = px.scatter( city,
    x= price,
    y= area,
    color='price'
     
)
st.plotly_chart(price_trend)


st.subheader('Listed by seller type')
seller_type = px.pie(city,seller_type)

st.plotly_chart(seller_type)

st.subheader('Listed by property type')
property_type = px.pie(city,property_type)

st.plotly_chart(property_type)


st.subheader('Price vs locality')
pvl = px.bar( city,
    x= locality,
    y= price, barmode='stack'
)
st.plotly_chart(pvl)

st.subheader('Sunchart for bedroom,bathroom,furnished types.')
bbf= px.sunburst( city, path=['bedroom','bathroom','furnish_type'] )
st.plotly_chart(bbf)


st.subheader('Data listed for reference')

st.dataframe(city)