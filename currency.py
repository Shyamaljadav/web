import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import requests
from bs4 import BeautifulSoup
from streamlit_lottie import st_lottie
def show_currency():
    st.markdown('<style> #footer{visibility}</style>', unsafe_allow_html=True)  

       
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    #lc = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_bczqkp40.json")
    #st_lottie(lc,height=300)
    #@st.cache
    st.write("""# Currency Conveter""")

    #@st.cache
    def read_data():
        url = "https://raw.githubusercontent.com/emrecanaltinsoy/forex_data/main/forex_usd_data.csv"
        data = pd.read_csv(url)
        cols = data.columns
        return data, cols[1:]


    # #@st.cache
    def scrape_currency():
        today = datetime.date.today()

        base_url = "https://www.x-rates.com/historical/?from=USD&amount=1&date"

        year = today.year
        month = today.month if today.month > 9 else f"0{today.month}"
        day = today.day if today.day > 9 else f"0{today.day}"

        URL = f"{base_url}={year}-{month}-{day}"

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        table = soup.find_all("tr")[12:]

        currencies = [table[i].text.split("\n")[1:3][0] for i in range(len(table))]
        currencies.insert(0, "date(y-m-d)")
        currencies.insert(1, "American Dollar")
        rates = [table[i].text.split("\n")[1:3][1] for i in range(len(table))]
        rates.insert(0, f"{year}-{month}-{day}")
        rates.insert(1, "1")
        curr_data = {currencies[i]: rates[i] for i in range(len(rates))}
        curr_data = pd.DataFrame(curr_data, index=[0])

        cols = curr_data.columns

        return curr_data, cols[1:]


    daily_df, columns = scrape_currency()
    base_curr = st.selectbox("Select the base currency", columns)
    selected_curr = st.multiselect("Select currencies", columns)
    amt =st.number_input("Enter amount to Convert:")
    if selected_curr:
        base = daily_df[base_curr].astype(float)

        selected = daily_df[selected_curr].astype(float)

        converted = selected / float(base)
        st.write(amt*converted)
        #st.write(converted)