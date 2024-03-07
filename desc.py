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
lottie_coding2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_calza6zj.json")
lottie_coding3 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_iacuyjna.json")
lottie_coding4 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_2gjZuP.json")
lottie_coding5 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_3rqwsqnj.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("ASSETS.AI :wave:")
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
    st.subheader("From series A to market domination we've got you cover.")
    st.write("##")
    text_column, image_column = st.columns((2, 1))
    with text_column:
        st.header("Experience")
        st.subheader("")
        st.write("##")
        st.write("##")

        st.header("Products")
        st.subheader("")
        st.write("##")
        st.write("##")

        st.header("Analizer")
        st.subheader("")
    with image_column:
        st_lottie(lottie_coding3, height=300, key="coding3")
        st.write("##")
        st.write("##")
        st_lottie(lottie_coding4, height=300, key="coding4")
        st.write("##")
        st.write("##")
        st_lottie(lottie_coding5, height=300, key="coding5")
        st.write("##")
        st.write("##")
        
        ##st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.header("")
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()