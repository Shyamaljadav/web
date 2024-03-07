import streamlit as st
from  streamlit_option_menu import option_menu
import pandas_datareader as data
from datetime import date
import datetime
import yaml
import database as db
import yfinance as yf 
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import requests
import pandas as pd 
import cufflinks as cf
import json
from PIL import Image
from newspaper import Article
from datetime import datetime as dt
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup
import io
from plotly import graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import nltk
import calendar
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
import subprocess
from streamlit_lottie import st_lottie
import lottie
import hydralit_components as hc
from login1 import show_login_page
import streamlit_authenticator as stauth
#from Home import user1
import streamlit as st
import mysql.connector


# Connect to the database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shiv1",
    database="assets"
)

cursor = conn.cursor()

# Create table if it doesn't exist
table_create_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""
cursor.execute(table_create_query)
conn.commit()

# Define the signup and login functions

    
    

    # Show the login/signup form
    # st.set_page_config(page_title="Login/Sign Up", page_icon=":guardsman:", layout="wide")


#st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)
bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("https://wallpapercave.com/wp/wp2128227.jpg");
background-size: cover;
background-repeat: no-repeat;
}}

"""
#st.markdown(bg_img,unsafe_allow_html=True)

    
hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# if 'logged' not in st.session_state:
#     st.session_state.logged = False
#else:
def user1():
    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Login":
        login()
    else:
        signup()

    # Close the database connection
    conn.close()

def signup():
    username = st.text_input("Username",key ='sql')
    password = st.text_input("Password", type='password',key ='sqlp')

    if st.button("Sign Up"):
        insert_query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
        cursor.execute(insert_query)
        conn.commit()
        st.success("Signup Successful!")


def login():
    import streamlit as st
    username = st.text_input("Username",key='sql')
    password = st.text_input("Password", type='password',key='sqlp')
    
    if st.button("Login"):
        select_query = f"SELECT * FROM users WHERE username='{username}' and password='{password}'"
        cursor.execute(select_query)
        result = cursor.fetchone()
        if result:
            
            #st.success("Login Successful!")
            #st.session_state['logged'] = True
    
#def home1():
            menu_data =[
                {'id':"home",'label':"Home",},
                {'id':"stocks",'label':"Stocks",'submenu':[{'id':"main",'label':"Main"},{'id':"pre",'label':"Prediction"},{'id':"sent",'label':"Sentiment",}]},
                {'id':"commodity",'label':"Commodity",'submenu':[{'id':"gold",'label':"Gold"},{'id':"silver",'label':"Silver"},{'id':"oil",'label':"Oil",}]},
                {'id':"land",'label':"Real Estate",'submenu':[{'id':"trend",'label':"Price Trend"},{'id':"rent",'label':"Rent"},]},
                {'id':"crypto",'label':"Crypto Currency",},
                {'id':"comm",'label':"Community",},
                {'id':"assist",'label':"Assistance",'submenu':[{'id':"assist1",'label':"Assistant"},{'id':"sum",'label':"Summarizer"}]},    
                {'id':"acc",'label':"Account",'submenu':[{'id':"user",'label':"User"},{'id':"dashboard",'label':"Dashboard"}]},
            ]

            menu_id = hc.nav_bar(
                menu_definition=menu_data,
                override_theme=None,
                home_name=None,
                login_name=None,
                hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
                sticky_nav=True, #at the top or not
                sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
            )

        #if menu_id =="stocks" or "gold" or "land" or "crypto" or "acc" or "assist" or "home":
        #if menu_id == "home":

            if menu_id == "home":
            
                selected = option_menu(
                menu_title=None,
                options=["Home","News","Currency Converter",],
                icons=None,
                orientation="horizontal",
                styles={
                    "container":{"padding":"0!important", "background-color":"orange"},
                    "icon":{"color":"black", "font-size":"15px"},
                    "nav-link":{
                        "font-size":"15px",
                        "text-align":"center",
                        "margin":"0px",
                        "--hover-color":"#eee",
                    },
                    "nav-link-selected":{"background-color":"grey"},    
                    },
                ) 
                #if selected =="Home" or "News" or "Currency Converter":          
                if selected =="Home":
                    import requests
                    import streamlit as st
                    from streamlit_lottie import st_lottie
                    from PIL import Image


                    #Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
                    #st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


                    def load_lottieurl(url):
                        r = requests.get(url)
                        if r.status_code != 200:
                            return None
                        return r.json()


                    # Use local CSS
                    def local_css(file_name):
                        with open(file_name) as f:
                            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


                    #local_css("style/style.css")

                    # ---- LOAD ASSETS ----
                    lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
                    lottie_coding2 = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_qam8tww4.json")
                    lottie_coding3 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_iacuyjna.json")
                    lottie_coding4 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_2gjZuP.json")
                    lottie_coding5 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_3rqwsqnj.json")
                    # img_contact_form = Image.open("images/yt_contact_form.png")
                    # img_lottie_animation = Image.open("images/yt_lottie_animation.png")

                    # ---- HEADER SECTION ----
                    with st.container():
                        st.subheader("ASSETS.AI :heavy_check_mark:")
                        st.title("A site for all your asset's exigency...")
                        left_column, right_column = st.columns(2)
                        with left_column:
                            st.write("##")
                            st.write("####")
                            st.subheader( "We're Assets.AI")
                            st.header("The all-in-one cumilative assets analysis software for those who seeks growth with ease.")
                        with right_column:
                            st_lottie(lottie_coding2, height=300, key="coding2")
                    # ---- BODY SECTION ----
                    with st.container():
                        st.write("---")
                        left_column, right_column = st.columns(2)
                        with right_column:
                            st.subheader("Our Pitch")
                            st.header(
                                """ We've Initiated our journey to become a SaaS based platform to provide users a seamless product adoptation and hassel free drive conversion. 
                                """
                            )
                        with left_column:
                            st_lottie(lottie_coding, height=300, key="coding")

                    # ---- PROJECTS ----
                    with st.container():
                        st.write("---")
                        st.write("#")
                        st.write("#")
                        st.subheader("From series A to market domination we've got you cover.")
                        st.write("#")

                        text_column, image_column = st.columns((2, 1))
                        with text_column:
                            st.header("Experience")
                            st.write("###")
                            st.subheader("With our services you will find some tasteful experience to handle and get endure of quality. The graph never turn down when it comes to us. We've made everything possible with emerging technologies. So, you never have to worry!")
                            st.write("#")
                            st.write("#")
                            st.write("#")
                            st.write("#")

                            st.header("Products")
                            st.write("###")
                            st.subheader("We've provided with enormous product line. Either you choose Stocks, Gold, Real Estate, Crypto... you can count on us. That's not all we're also commited to our clients and customers as the time passes new products will be introduced.")
                            st.write("#")
                            st.write("#")
                            st.write("#")
                            st.write("#")

                            st.header("Analyzer")
                            st.write("###")
                            st.subheader("Wait, no dashboard?  Nooo way! we've also provided the much needed dashboard. Where you can insert all your required details and can analyse all possiblities and strategies with visualisation. So, you never get slow with the trend.")
                        with image_column:
                            st_lottie(lottie_coding3, height=350, key="coding3")
                            st.write("##")
                            st.write("##")
                            st_lottie(lottie_coding4, height=350, key="coding4")
                            st.write("##")
                            st.write("##")
                            st_lottie(lottie_coding5, height=350, key="coding5")
                            st.write("##")
                            st.write("##")
                            
                            ##st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
                    with st.container():
                        st.write("___")
                        left_column, mid_column, right_column = st.columns(3)
                        with left_column:
                            st.header("me")
                        with mid_column:
                            st.subheader("shyamal")
                        with right_column:
                            st.subheader("kevin")    


                    with st.container():
                        st.write("---")
                        text_column, image_column = st.columns((2, 1))
                        with text_column:
                            st.subheader("“I will tell you how to become rich. Close the doors. Be fearful when others are greedy. Be greedy when others are fearful.” ")
                            st.write("-Warren Buffett")
                            st.write("##")        
                        with image_column:
                            st.write("image of warren buffet")


                    # ---- CONTACT ----
                    with st.container():
                        st.write("---")
                        st.header("Let's Explore more Together!")
                        st.write("##")
                        st.subheader("More Informations? Say hello")
                        st.subheader("Contact Us")
                    #link for email id
                        st.write("##")

                        left_column, right_column = st.columns(2)
                        with left_column:
                            st.write("email")
                            st.write("address")
                            st.write("phone no.")

                        with right_column:
                            st.write("all links for different handles")

                if selected == "News":

                    nltk.download('punkt')
                    def fetch_news_search_topic(topic):
                        site = 'https://news.google.com/rss/search?q={}'.format(topic)
                        op = urlopen(site)  # Open that site
                        rd = op.read()  # read data from site
                        op.close()  # close the object
                        sp_page = soup(rd, 'xml')  # scrapping data from site
                        news_list = sp_page.find_all('item')  # finding news
                        return news_list

                    def fetch_top_news():
                        site = 'https://news.google.com/news/rss'
                        op = urlopen(site)  # Open that site
                        rd = op.read()  # read data from site
                        op.close()  # close the object
                        sp_page = soup(rd, 'xml')  # scrapping data from site
                        news_list = sp_page.find_all('item')  # finding news
                        return news_list


                    def fetch_category_news(topic):
                        site = 'https://news.google.com/news/rss/headlines/section/topic/{}'.format(topic)
                        op = urlopen(site)  # Open that site
                        rd = op.read()  # read data from site
                        op.close()  # close the object
                        sp_page = soup(rd, 'xml')  # scrapping data from site
                        news_list = sp_page.find_all('item')  # finding news
                        return news_list


                    def fetch_news_poster(poster_link):
                        try:
                            u = urlopen(poster_link)
                            raw_data = u.read()
                            image = Image.open(io.BytesIO(raw_data))
                            st.image(image, use_column_width=True)
                        except:
                            st.write("No image for this News is Available")
                            #image = Image.open('./Meta/no_image.jpg')
                        # st.image(image, use_column_width=True)
                            


                    def display_news(list_of_news, news_quantity):
                        c = 0
                        for news in list_of_news:
                            c += 1
                            # st.markdown(f"({c})[ {news.title.text}]({news.link.text})")
                            st.write('**({}) {}**'.format(c, news.title.text))
                            news_data = Article(news.link.text)
                            try:
                                news_data.download()
                                news_data.parse()
                                news_data.nlp()
                            except Exception as e:
                                st.error(e)
                            fetch_news_poster(news_data.top_image)
                            with st.expander(news.title.text):
                                st.markdown(
                                    '''<h6 style='text-align: justify;'>{}"</h6>'''.format(news_data.summary),
                                    unsafe_allow_html=True)
                                st.markdown("[Read more at {}...]({})".format(news.source.text, news.link.text))
                            st.success("Published Date: " + news.pubDate.text)
                            if c >= news_quantity:
                                break


                    
                    st.title("News: A Summarised News📰")
                    #image = Image.open('./Meta/newspaper.png')
                    
                    col1, col2, col3 = st.columns([3, 5, 3])

                    with col1:
                        st.write("")

                # with col2:
                    #  st.image(image, use_column_width=False)

                    with col3:
                        st.write("")
                    category = ['--Select--', 'Trending News', 'Favourite Topics', 'Search Topic']
                    cat_op = st.selectbox('Select your Category', category)
                    if cat_op == category[0]:
                        st.warning('Please select Type!!')
                    elif cat_op == category[1]:
                        st.subheader("✅ Here is the Trending🔥 news for you")
                        no_of_news = 15#st.slider('Number of News:', min_value=5, max_value=25, step=1)
                        news_list = fetch_top_news()
                        display_news(news_list, no_of_news)
                    elif cat_op == category[2]:
                        av_topics = ['Choose Topic', 'WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS', 'SCIENCE',
                                    'HEALTH']
                        st.subheader("Choose your favourite Topic")
                        chosen_topic = st.selectbox("Choose your favourite Topic", av_topics)
                        if chosen_topic == av_topics[0]:
                            st.warning("Please Choose the Topic")
                        else:
                            no_of_news = 15#st.slider('Number of News:', min_value=5, max_value=25, step=1)
                            news_list = fetch_category_news(chosen_topic)
                            if news_list:
                                st.subheader("✅ Here are the some {} News for you".format(chosen_topic))
                                display_news(news_list, no_of_news)
                            else:
                                st.error("No News found for {}".format(chosen_topic))

                    elif cat_op == category[3]:
                        user_topic = st.text_input("Enter your Topic🔍")
                        no_of_news = 15 #st.slider('Number of News:', min_value=5, max_value=15, step=1)

                        if st.button("Search") and user_topic != '':
                            user_topic_pr = user_topic.replace(' ', '')
                            news_list = fetch_news_search_topic(topic=user_topic_pr)
                            if news_list:
                                st.subheader("✅ Here are the some {} News for you".format(user_topic.capitalize()))
                                display_news(news_list, no_of_news)
                            else:
                                st.error("No News found for {}".format(user_topic))
                        else:
                            st.warning("Please write Topic Name to Search🔍")
                    

                if selected =="Crypto Currency":

                    import streamlit as st
                    from streamlit_lottie import st_lottie
                    import requests

                    def load_lottieurl(url):
                        r = requests.get(url)
                        if r.status_code != 200:
                            return None
                        return r.json()

                    lc = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_bczqkp40.json")
                    st.markdown('<iframe src="https://embed.lottiesfiles.com/animation/9888"></iframe>', unsafe_allow_html=True)

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        curr1 =  st.selectbox('Currency 1',['EUR', 'USD', 'GBP'])
                    with col2:
                        if curr1 == 'EUR':
                            st_lottie(lc,height=200,key="abc")
                        elif curr1 == 'USD':
                            st.markdown('<iframe src="https://embed.lottiefiles.com/animation/89427"></iframe>', unsafe_allow_html=True)
                        else:
                            st.markdown('<iframe src="https://embed.lottiefiles.com/animation/89429"></iframe>', unsafe_allow_html=True)
                    with col3:
                        curr2 =  st.selectbox('Currency 2',['USD', 'EUR', 'GBP'])

                    url = f'https://free.currconv.com/api/v7/convert?q={curr1}_{curr2},{curr2}_{curr1}&compact=ultra&apiKey=[YOUR_API_KEY]'

                    r = requests.get(url)
                    r = r.json()
                    one_two = r[f"{curr1}_{curr2}"]
                    two_one = r[f"{curr2}_{curr1}"]

                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"1 {curr1} to {curr2}")
                        st.success(one_two)
                    with col2:
                        st.write(f"1 {curr2} to {curr1}")
                        st.success(two_one)

                    col1 ,col2 = st.columns(2)
                    with col1:
                        amt = st.number_input(curr1)
                    with col2:
                        converted = amt*one_two
                        st.text('Converted Amount')
                        st.success(converted)

                        st.markdown('<style> #footer{visibility}</style>', unsafe_allow_html=True)  
            #if 'logged' not in st.session_state:
            #   st.session_state['logged']= False
            #  show_home()



            if menu_id == "main":
                def main():

                    #st.set_page_config(
                    #    page_title="Stocks.AI",
                    #    layout="wide",
                    #   initial_sidebar_state="auto",
                    #    menu_items={
                    #        "Get Help": "https://github.com/smaranjitghose/PyFinAnalytics/",
                    #        "Report a bug": "https://github.com/smaranjitghose/PyFinAnalytics/issues",
                    #        "About": "# This app serves is an MVP for interactive dashboards that can be used for financial data analysis instead of Microsoft Excel",
                    #    },
                    #)

                    st.title("StockAI")

                    start_date = st.date_input(
                        "Start Date",
                        min_value=datetime(2000, 1, 1),
                        max_value=datetime.today(),
                        help="Enter the date from which you want to analyse the stock data",
                    )
                    end_date = st.date_input(
                        "End Date",
                        min_value=start_date,
                        max_value=datetime.today(),
                        help="Enter the date till which you want to analyse the stock data",
                    )
                    if start_date >= end_date:
                        st.warning(
                            "You seem to have selected a start date greater than or equals to end date. Please reselect the dates"
                        )

                    url = 'https://drive.google.com/file/d/1QK5XmrztKAUM4Pu3Fy2dbKPFwhUuJDa9/view?usp=share_link'
                    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
                    ticker_list = pd.read_csv(path)
                    ticker = st.selectbox('Select Ticker',ticker_list)

                    if st.button("Get Market Data"):
                        
                        stock_data = fetch_stock_data(ticker, start_date, end_date)

                        # Display the stock data
                        st.dataframe(stock_data)
                        # Basic closing price analysis
                        basic_closing_price_analysis(stock_data, ticker)
                        # Compute Daily Change Percentage
                        st.markdown(" ")
                        st.markdown("### Daily Change Percentage")
                        stock_data = get_daiy_change(stock_data)
                        st.dataframe(
                            stock_data.style.set_na_rep("Not Available").highlight_null(
                                null_color="orange"
                            )
                        )
                        # Plot Daily Change Percentage
                        plot_daily_change(stock_data, ticker)
                        # Compute Log Returns
                        st.markdown("#### Log Returns")
                        stock_data = get_log_returns(stock_data)
                        st.dataframe(stock_data)
                        # Compute Beta
                        st.markdown("#### Beta")
                        beta = get_beta(ticker, start_date, end_date)
                        st.write(f"Beta for {ticker} is {round(beta,4)}")
                        # Compute Volatility
                        st.markdown("#### Volatility")
                        volatility = get_volatility(stock_data)
                        st.write(f"Volatility for {ticker} is {round(volatility,4)}")
                        # Compute 10 Day Moving Average
                        st.markdown(" ")
                        st.markdown("#### 10 Day Moving Average:")
                        stock_data = get_10_day_ma(stock_data)
                        st.dataframe(stock_data)
                        # Plot 10 Day Moving Average
                        st.markdown(" ")
                        st.markdown("#### 10 Day Moving Average Plot:")
                        plot_10_day_ma(stock_data, ticker)
                        # Compute 10 Day Exponential Moving Average
                        st.markdown(" ")
                        st.markdown("#### 10 Day Exponential Moving Average:")
                        stock_data = get_10_day_ema(stock_data)
                        st.dataframe(stock_data)
                        # Plot 10 Day Exponential Moving Average
                        st.markdown(" ")
                        st.markdown("#### 10 Day Exponential Moving Average Plot:")
                        plot_10_day_ema(stock_data, ticker)
                        # Trend Analysis using Moving Average
                        st.markdown(" ")
                        st.markdown("#### Trend Analysis using Moving Averages:")
                        trend_analysis_ma(stock_data, ticker)
                        # MACD
                        st.markdown(" ")
                        st.markdown("#### MACD:")
                        get_macd(stock_data, ticker)
                        # Stochastic Oscillator
                        st.markdown(" ")
                        st.markdown("#### Stochastic Oscillator:")
                        get_stochastic_oscillator(stock_data, ticker)
                        
                    


                def fetch_stock_data(ticker, start_date, end_date):
                    """
                    Fetch stock data from Yahoo Finance
                    """
                    stock_data = pdr.get_data_yahoo(ticker, start_date, end_date)
                    return stock_data


                def basic_closing_price_analysis(stock_data, ticker):
                    # Display minimum and maximum closing prices in the selected date range
                    max_closing_price = stock_data["Close"].max()
                    max_date = stock_data[stock_data["Close"] == max_closing_price].index[0]
                    st.markdown(f"### Maximum closing price: {round(max_closing_price,4)}")
                    st.markdown(f"Maximum Closing Price was observed on {max_date}")
                    min_closing_price = stock_data["Close"].min()
                    min_date = stock_data[stock_data["Close"] == min_closing_price].index[0]
                    st.markdown(f"### Minimum closing price was: {round(min_closing_price,4)}")
                    st.markdown(f"Minimum Closing Price was observed on {min_date}")
                    # Plot movement of closing price
                    fig, ax = plt.subplots(figsize=(10, 5))
                    ax = fig.add_subplot(111)
                    ax.plot(stock_data["Close"])
                    ax.set_title(f"{ticker} stock price movement")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)


                def get_daiy_change(stock_data):
                    stock_data["Daily Change"] = stock_data["Close"].pct_change() * 100
                    return stock_data


                def plot_daily_change(stock_data, ticker):
                    # Plot the daily change percentage
                    st.markdown(" ")
                    st.markdown("### Daily Change Plot")
                    fig = plt.figure(figsize=(10, 3))
                    ax = fig.add_subplot(111)
                    ax.plot(stock_data["Daily Change"])
                    ax.set_title(f"Daily Changes for {ticker}")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)
                    # Plot Daily Change Percentage Histogram
                    st.markdown(" ")
                    st.markdown("#### Daily Change Plot (Histogram)")
                    fig = plt.figure(figsize=(10, 3))
                    ax = fig.add_subplot(111)
                    ax.hist(stock_data["Daily Change"], bins=100)
                    ax.set_title(f"Daily Changes for {ticker}")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)


                def get_beta(ticker, start_date, end_date):
                    tickers = [ticker, "^GSPC"]
                    stock_data = pdr.get_data_yahoo(
                        tickers, start=start_date, end=end_date, interval="m"
                    )
                    stock_data = stock_data["Adj Close"]
                    log_returns = np.log(stock_data / stock_data.shift())
                    cov = log_returns.cov()
                    var = log_returns["^GSPC"].var()
                    beta = cov.loc[ticker, "^GSPC"] / var
                    return beta


                def get_log_returns(stock_data):
                    stock_data["Log Returns"] = np.log(
                        stock_data["Close"] / stock_data["Close"].shift(1)
                    )
                    return stock_data


                def get_volatility(stock_data):
                    return stock_data["Log Returns"].std() * np.sqrt(252)


                def get_10_day_ma(stock_data):
                    stock_data["MA10"] = stock_data["Close"].rolling(10).mean()
                    return stock_data


                def plot_10_day_ma(stock_data, ticker):
                    fig, ax = plt.subplots(figsize=(10, 3))
                    ax.plot(stock_data["MA10"])
                    ax.set_title(f"10 Day Moving Average for {ticker}")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)


                def get_10_day_ema(stock_data):
                    stock_data["EMA10"] = stock_data["Close"].ewm(span=10, adjust=False).mean()
                    return stock_data


                def plot_10_day_ema(stock_data, ticker):
                    fig, ax = plt.subplots(figsize=(10, 3))
                    ax.plot(stock_data["EMA10"])
                    ax.set_title(f"10 Day Exponential Moving Average for {ticker}")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)


                def trend_analysis_ma(stock_data, ticker):
                    fig, ax = plt.subplots(figsize=(10, 3))
                    ax.plot(stock_data["MA10"], label="MA10")
                    ax.plot(stock_data["EMA10"], label="EMA10")
                    ax.plot(stock_data["Close"], label="Close")
                    ax.legend()
                    ax.set_title(f"Trend Analysis using Moving Average for {ticker}")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)


                def get_macd(stock_data, ticker):
                    exp1 = stock_data["Close"].ewm(span=12, adjust=False).mean()
                    exp2 = stock_data["Close"].ewm(span=26, adjust=False).mean()
                    stock_data["MACD"] = exp1 - exp2
                    stock_data["Signal Line"] = stock_data["MACD"].ewm(span=9, adjust=False).mean()
                    fig, ax = plt.subplots(figsize=(10, 3))
                    ax.plot(stock_data["MACD"], label="MACD")
                    ax.plot(stock_data["Signal Line"], label="Signal Line")
                    ax.legend()
                    ax.set_title(f"MACD and Signal Line for {ticker}")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)


                def get_stochastic_oscillator(stock_data, ticker):
                    high14 = stock_data["High"].rolling(14).max()
                    low14 = stock_data["Low"].rolling(14).min()
                    stock_data["%K"] = (stock_data["Close"] - low14) * 100 / (high14 - low14)
                    stock_data["%D"] = stock_data["%K"].rolling(3).mean()
                    fig, ax = plt.subplots(figsize=(10, 3))
                    ax.plot(stock_data["%K"], label="%K")
                    ax.plot(stock_data["%D"], label="%D")
                    ax.axhline(80, c="purple", alpha=0.5)
                    ax.axhline(20, c="green", alpha=0.5)
                    ax.legend()
                    ax.set_title(f"Stochastic Oscillator for {ticker}")
                    ax.set_xlabel("Date")
                    ax.grid(True)
                    st.pyplot(fig)

                if __name__ == "__main__":
                    main()
                
            if menu_id =="pre":
                START = "2015-01-01"
                TODAY = date.today().strftime("%Y-%m-%d")

                st.title("Stock Prediction")


                url = 'https://drive.google.com/file/d/1QK5XmrztKAUM4Pu3Fy2dbKPFwhUuJDa9/view?usp=share_link'
                path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]



                stocks =  pd.read_csv(path)
                selected_stock = st.selectbox("Select dataset for prediction", stocks)

                n_years = st.slider("Years of prediction", 1 , 4)
                period = n_years * 365

                @st.cache
                def load_data(ticker):
                    data = yf.download(ticker, START, TODAY)
                    data.reset_index(inplace = True)
                    return data

                data_load_state = st.text("Load data...")
                data = load_data(selected_stock)
                data_load_state.text("Loading data...done!")

                st.subheader('Raw data')
                st.write(data.tail())

                def plot_raw_data():
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
                    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
                    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
                    st.plotly_chart(fig)

                plot_raw_data()

                df_train = data[['Date','Close']]
                df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

                m = Prophet()
                m.fit(df_train)
                future = m.make_future_dataframe(periods=period)
                forecast = m.predict(future)

                st.subheader('Forecast data')
                st.write(forecast.tail())

                st.write('forecast data')
                fig1 = plot_plotly(m, forecast)
                st.plotly_chart(fig1)

                st.write('forecast components')
                fig2 = m.plot_components(forecast)
                st.write(fig2)

            if menu_id =="sent":
                #st.set_page_config(page_title = "Stock News Sentiment Analyzer", layout = "wide")

                def get_news(ticker):
                    url = finviz_url + ticker
                    req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}) 
                    response = urlopen(req)    
                    # Read the contents of the file into 'html'
                    html = soup(response)
                    # Find 'news-table' in the Soup and load it into 'news_table'
                    news_table = html.find(id='news-table')
                    return news_table
                    
                # parse news into dataframe
                def parse_news(news_table):
                    parsed_news = []
                    
                    for x in news_table.findAll('tr'):
                        # occasionally x (below) may be None when the html table is poorly formatted, skip it in try except instead of throwing an error and exiting
                        # may also use an if loop here to check if x is None first	
                        try:
                            # read the text from each tr tag into text
                            # get text from a only
                            text = x.a.get_text() 
                            # splite text in the td tag into a list 
                            date_scrape = x.td.text.split()
                            # if the length of 'date_scrape' is 1, load 'time' as the only element

                            if len(date_scrape) == 1:
                                time = date_scrape[0]				
                            # else load 'date' as the 1st element and 'time' as the second    
                            else:
                                date = date_scrape[0]
                                time = date_scrape[1]
                            
                            # Append ticker, date, time and headline as a list to the 'parsed_news' list
                            parsed_news.append([date, time, text])        
                            
                            
                        except:
                            pass
                            
                    # Set column names
                    columns = ['date', 'time', 'headline']
                    # Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
                    parsed_news_df = pd.DataFrame(parsed_news, columns=columns)        
                    # Create a pandas datetime object from the strings in 'date' and 'time' column
                    parsed_news_df['datetime'] = pd.to_datetime(parsed_news_df['date'] + ' ' + parsed_news_df['time'])
                            
                    return parsed_news_df
                        
                    
                        
                def score_news(parsed_news_df):
                    # Instantiate the sentiment intensity analyzer
                    vader = SentimentIntensityAnalyzer()
                    
                    # Iterate through the headlines and get the polarity scores using vader
                    scores = parsed_news_df['headline'].apply(vader.polarity_scores).tolist()

                    # Convert the 'scores' list of dicts into a DataFrame
                    scores_df = pd.DataFrame(scores)

                    # Join the DataFrames of the news and the list of dicts
                    parsed_and_scored_news = parsed_news_df.join(scores_df, rsuffix='_right')             
                    parsed_and_scored_news = parsed_and_scored_news.set_index('datetime')    
                    parsed_and_scored_news = parsed_and_scored_news.drop(['date', 'time'], 1)          
                    parsed_and_scored_news = parsed_and_scored_news.rename(columns={"compound": "sentiment_score"})

                    return parsed_and_scored_news

                def plot_hourly_sentiment(parsed_and_scored_news, ticker):
                
                    # Group by date and ticker columns from scored_news and calculate the mean
                    mean_scores = parsed_and_scored_news.resample('H').mean()

                    # Plot a bar chart with plotly
                    fig = px.bar(mean_scores, x=mean_scores.index, y='sentiment_score', title = ticker + ' Hourly Sentiment Scores')
                    return fig # instead of using fig.show(), we return fig and turn it into a graphjson object for displaying in web page later

                def plot_daily_sentiment(parsed_and_scored_news, ticker):
                
                    # Group by date and ticker columns from scored_news and calculate the mean
                    mean_scores = parsed_and_scored_news.resample('D').mean()

                    # Plot a bar chart with plotly
                    fig = px.bar(mean_scores, x=mean_scores.index, y='sentiment_score', title = ticker + ' Daily Sentiment Scores')
                    return fig # instead of using fig.show(), we return fig and turn it into a graphjson object for displaying in web page later

                # for extracting data from finviz
                finviz_url = 'https://finviz.com/quote.ashx?t='


                st.header("Stock News Sentiment Analyzer")

                ticker = st.text_input('Enter Stock Ticker', '').upper()

                df = pd.DataFrame({'datetime': datetime.now(), 'ticker': ticker}, index = [0])


                try:
                    st.subheader("Hourly and Daily Sentiment of {} Stock".format(ticker))
                    news_table = get_news(ticker)
                    parsed_news_df = parse_news(news_table)
                    print(parsed_news_df)
                    parsed_and_scored_news = score_news(parsed_news_df)
                    fig_hourly = plot_hourly_sentiment(parsed_and_scored_news, ticker)
                    fig_daily = plot_daily_sentiment(parsed_and_scored_news, ticker) 
                    
                    st.plotly_chart(fig_hourly)
                    st.plotly_chart(fig_daily)

                    description = """
                        The above chart averages the sentiment scores of {} stock hourly and daily.
                        The table below gives each of the most recent headlines of the stock and the negative, neutral, positive and an aggregated sentiment score.
                        The news headlines are obtained from the FinViz website.
                        Sentiments are given by the nltk.sentiment.vader Python library.
                        """.format(ticker)
                        
                    st.write(description)	 
                    st.table(parsed_and_scored_news)
                    
                except Exception as e:
                    print(str(e))
                    st.write("Enter a correct stock ticker, e.g. 'AAPL' above and hit Enter.")	

                hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
                st.markdown(hide_streamlit_style, unsafe_allow_html=True)
                



                    
            if menu_id == "gold":
                
                START = "04-01-2000"
                END = "01-09-2022"

                st.title("Gold Price Prediction")

                url = 'https://drive.google.com/file/d/1duvRDQagUYGT1c_Imd0ZJVgEnucBniV7/view?usp=share_link'
                path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
                data = pd.read_csv(path)
                data.head()

                st.subheader('Raw data')
                st.write(data.tail())

                def plot_raw_data():
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='gold_close'))
                    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
                    st.plotly_chart(fig)

                plot_raw_data()


                df_train = data[['Date','Close']]
                df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

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
                    

            #if menu_id == "land":

            if menu_id =="trend":
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

            if menu_id =="rent":
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
                
                    

            if menu_id == "crypto":

                st.markdown('''# **CryptoAI**
                A simple way to get the Cryptoc prices... ''')

                st.header('**Select Price**')

                df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

                def round_value(input_value):
                    if input_value.values > 1:
                        a = float(round(input_value, 2))
                    else:
                        a = float(round(input_value, 8))
                    return a

                col1, col2, col3 = st.columns(3)

            # Widget (Cryptocurrency selection box)
                col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
                col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
                col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )
                col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD') )
                col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
                col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
                col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
                col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('DOTBUSD') )
                col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD') )

            # DataFrame of selected Cryptocurrency
                col1_df = df[df.symbol == col1_selection]
                col2_df = df[df.symbol == col2_selection]
                col3_df = df[df.symbol == col3_selection]
                col4_df = df[df.symbol == col4_selection]
                col5_df = df[df.symbol == col5_selection]
                col6_df = df[df.symbol == col6_selection]
                col7_df = df[df.symbol == col7_selection]
                col8_df = df[df.symbol == col8_selection]
                col9_df = df[df.symbol == col9_selection]

            # Apply a custom function to conditionally round values
                col1_price = round_value(col1_df.weightedAvgPrice)
                col2_price = round_value(col2_df.weightedAvgPrice)
                col3_price = round_value(col3_df.weightedAvgPrice)
                col4_price = round_value(col4_df.weightedAvgPrice)
                col5_price = round_value(col5_df.weightedAvgPrice)
                col6_price = round_value(col6_df.weightedAvgPrice)
                col7_price = round_value(col7_df.weightedAvgPrice)
                col8_price = round_value(col8_df.weightedAvgPrice)
                col9_price = round_value(col9_df.weightedAvgPrice)

            # Select the priceChangePercent column
                col1_percent = f'{float(col1_df.priceChangePercent)}%'
                col2_percent = f'{float(col2_df.priceChangePercent)}%'
                col3_percent = f'{float(col3_df.priceChangePercent)}%'
                col4_percent = f'{float(col4_df.priceChangePercent)}%'
                col5_percent = f'{float(col5_df.priceChangePercent)}%'
                col6_percent = f'{float(col6_df.priceChangePercent)}%'
                col7_percent = f'{float(col7_df.priceChangePercent)}%'
                col8_percent = f'{float(col8_df.priceChangePercent)}%'
                col9_percent = f'{float(col9_df.priceChangePercent)}%'

            # Create a metrics price box
                col1.metric(col1_selection, col1_price, col1_percent)
                col2.metric(col2_selection, col2_price, col2_percent)
                col3.metric(col3_selection, col3_price, col3_percent)
                col1.metric(col4_selection, col4_price, col4_percent)
                col2.metric(col5_selection, col5_price, col5_percent)
                col3.metric(col6_selection, col6_price, col6_percent)
                col1.metric(col7_selection, col7_price, col7_percent)
                col2.metric(col8_selection, col8_price, col8_percent)
                col3.metric(col9_selection, col9_price, col9_percent)

                st.header('**All Price**')
                st.dataframe(df)




            # if menu_id == "user":
                
                #show_logout_page()        
                    
                        
                        
            if menu_id == "dashboard":

                incomes = ["Salary", "Other Income"]
                expenses = ["stocks","gold","real estate", "crypto", "forex", "cash"]
                currency = "INR"
                page_title = "Assets diverse Dashboard"
                page_icon = ":money_with_wings:"
                layout = "wide"

                #st.set_page_config(page_title=page_title,page_icon=page_icon, layout=layout)
                st.title(page_title+""+page_icon)

                years = [dt.today().year, dt.today().year+1]
                months = list(calendar.month_name[1:])


                def get_all_periods():
                    items = db.fetch_all_periods()
                    periods = [item["key"] for item in items]
                    return periods


                hide_st_style = """
                            <style>
                            #MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}
                            header {visibility: hidden;}
                            </style>
                            """
                st.markdown(hide_st_style, unsafe_allow_html=True)

                selected = option_menu(
                    menu_title=None,
                    options= ["Data Entry","Data Visualization"],
                    #icons=["pencil-fill","bar-chart-fill"],
                    orientation="horizontal",
                    styles={
                    "container":{"padding":"0!important", "background-color":"orange"},
                    "icon":{"color":"black", "font-size":"15px"},
                    "nav-link":{
                        "font-size":"15px",
                        "text-align":"center",
                        "margin":"0px",
                        "--hover-color":"#eee",
                    },
                    "nav-link-selected":{"background-color":"grey"},    
                    },
                )

                if selected == "Data Entry":

                    st.header(f"Data Entry in {currency}")
                    with st.form("entry_form", clear_on_submit=True):
                        col1,col2 = st.columns(2)
                        col1.selectbox("Select Month:",months,key= "month")
                        col2.selectbox("Select Year:", years, key= "year" )

                        "___"
                        with st.expander("Income"):
                            for income in incomes:
                                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
                        with st.expander("Expenses"):
                            for expense in expenses:
                                st.number_input(f"{expense}", min_value=0, format="%i", step=10, key=expense)
                        with st.expander("Comment"):
                            comment = st.text_area("",placeholder="Enter a comment here...")

                        "___"
                        submitted = st.form_submit_button("Save Data")
                        if submitted:
                            period = str(st.session_state["year"])+ "_"+ str(st.session_state["month"])
                            incomes = {income: st.session_state[income] for income in incomes}
                            expenses = {expense: st.session_state[expense] for expense in expenses}
                            db.insert_period(period, incomes, expenses, comment)
                            st.success("Data saved!")


                if selected == "Data Visualization":
                    st.header("Data Visualization")
                    with st.form("saved_periods"):
                        period = st.selectbox("Select Period:", get_all_periods())
                        submitted = st.form_submit_button("Plot Period")
                        if submitted:
                            # Get data from database
                            period_data = db.get_period(period)
                            comment = period_data.get("comment")
                            expenses = period_data.get("expenses")
                            incomes = period_data.get("incomes")

                            # Create metrics
                            total_income = sum(incomes.values())
                            total_expense = sum(expenses.values())
                            remaining_budget = total_income - total_expense
                            col1, col2, col3 = st.columns(3)
                            col1.metric("Total Income", f"{total_income} {currency}")
                            col2.metric("Total Expense", f"{total_expense} {currency}")
                            col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
                            st.text(f"Comment: {comment}")

                            # Create sankey chart
                            label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
                            source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
                            target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
                            value = list(incomes.values()) + list(expenses.values())

                            # Data to dict, dict to sankey
                            link = dict(source=source, target=target, value=value)
                            node = dict(label=label, pad=20, thickness=30, color="#E694FF")
                            data = go.Sankey(link=link, node=node)

                            # Plot it!
                            fig = go.Figure(data)
                            fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
                            st.plotly_chart(fig, use_container_width=True)

            if menu_id =="assist1":
                import openai 
                import streamlit as st
                from streamlit_chat import message 

                openai.api_key = st.secrets["pass"]

                def generate_response(prompt):
                    completions = openai.Completion.create(
                        engine = "text-davinci-003",
                        prompt = prompt,
                        max_tokens = 1024,
                        n = 1,
                        stop = None,
                        temperature=0.5,
                    )
                    message = completions.choices[0].text
                    return message

                st.title("chatBot : Streamlit + openAI")

                # Storing the chat
                if 'generated' not in st.session_state:
                    st.session_state['generated'] = []

                if 'past' not in st.session_state:
                    st.session_state['past'] = []

                # We will get the user's input by calling the get_text function
                def get_text():
                    input_text = st.text_input("You: ","Hello, how are you?", key="input")
                    return input_text

                user_input = get_text()

                if user_input:
                    output = generate_response(user_input)
                    # store the output 
                    st.session_state.past.append(user_input)
                    st.session_state.generated.append(output)

                if st.session_state['generated']:
                    
                    for i in range(len(st.session_state['generated'])-1, -1, -1):
                        message(st.session_state["generated"][i], key=str(i))
                        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
                                
            if menu_id =="sum":
                import openai
                import streamlit as st

                openai.api_key = st.secrets["pass"]

                article_text = st.text_area("Enter your scientific texts to summarize")
                output_size = st.radio(label = "What kind of output do you want?", 
                                    options= ["To-The-Point", "Concise", "Detailed"])

                if output_size == "To-The-Point":
                    out_token = 50
                elif output_size == "Concise":
                    out_token = 128
                else:
                    out_token = 516

                if len(article_text)>100:
                    if st.button("Generate Summary",type='primary'):
                    
                        response = openai.Completion.create(
                            engine="text-davinci-003",
                            prompt="Please summarize this scientific article for me in a few sentences: " + article_text,
                            max_tokens = out_token,
                            temperature = 0.5,
                        )
                        
                        res = response["choices"][0]["text"]
                        st.success(res)
                        st.download_button('Download result', res)
                else:
                    st.warning("Not enough words to summarize!")



            if menu_id =="comm":
                # if 'logged in' not in st.session_state:
                #     st.session_state['logged in'] = False
                    show_login_page()


            
        else:
            st.error("Wrong username or password")


user1()