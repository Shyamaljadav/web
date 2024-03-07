import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lc = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_bczqkp40.json")
