import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


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