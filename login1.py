import pyrebase 
import streamlit as st
from datetime import datetime
from streamlit_lottie import st_lottie
import requests
 


firebaseConfig = {
  'apiKey': "AIzaSyCZ-4FMM2mY_Q8Qqi9t0N0CMTeTkmuLGZA",
  'authDomain': "assets-ai.firebaseapp.com",
  'projectId': "assets-ai",
  'databaseURL':'https://assets-ai-default-rtdb.firebaseio.com/',
  'storageBucket': "assets-ai.appspot.com",
  'messagingSenderId': "775392806417",
  'appId': "1:775392806417:web:34ed859d97136ce8ccd3b0",
  'measurementId': "G-TNZXSWZC06"
}
def show_login_page():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    # Database
    db = firebase.database()
    storage = firebase.storage()
    st.title("Assets.AI Community")



    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding_lo = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_gjmecwii.json")

    left_column, right_column = st.columns(2)
    with left_column:
        
        st_lottie(lottie_coding_lo, height=300, key="coding_lo")

        st.subheader("Seems like you haven't logged in! Explore more features by Log in...")




    with right_column:
        
        # Authentication
        choice = st.selectbox('login/Signup', ['Login', 'Sign up'])

        # Obtain User Input for email and password
        email = st.text_input('Please enter your email address',key='fire')
        password = st.text_input('Please enter your password',type = 'password', key='firep')


        if choice == 'Sign up':
            handle = st.text_input( 
                'Please input your app handle name', value='Default')
            submit = st.button('Create my account')

            if submit:
                user = auth.create_user_with_email_and_password(email, password)
                st.success('Your account is created suceesfully!')
                st.balloons()
                # Sign in
                user = auth.sign_in_with_email_and_password(email, password)
                db.child(user['localId']).child("Handle").set(handle)
                db.child(user['localId']).child("ID").set(user['localId'])
                st.title('Welcome' + handle)
                st.info('Login via login drop down selection')

        # Login Block
        if choice == 'Login':
            login = st.checkbox('Login')
            if login:
                user = auth.sign_in_with_email_and_password(email,password)
                # if 'logged in' not in st.session_state:
                #     st.session_state['logged in']= True
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                bio = st.radio('Jump to',['Home','Workplace Feeds', 'Settings'])
                
        # SETTINGS PAGE 
                if bio == 'Settings':  
                    # CHECK FOR IMAGE
                    nImage = db.child(user['localId']).child("Image").get().val()    
                    # IMAGE FOUND     
                    if nImage is not None:
                        # We plan to store all our image under the child image
                        Image = db.child(user['localId']).child("Image").get()
                        for img in Image.each():
                            img_choice = img.val()
                            #st.write(img_choice)
                        st.image(img_choice,width=300)
                        exp = st.expander('Change Bio and Image')  
                        # User plan to change profile picture  
                        with exp:
                            newImgPath = st.file_uploader("Upload file", type=["csv", "png", "jpg"])#st.text_input('Enter full path of your profile imgae')
                            upload_new = st.button('Upload')
                            if upload_new:
                                uid = user['localId']
                                fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                                a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                                db.child(user['localId']).child("Image").push(a_imgdata_url)
                                st.success('Success!')           
                    # IF THERE IS NO IMAGE
                    else:    
                        st.info("No profile picture yet")
                        newImgPath = st.file_uploader("Upload file", type=["csv", "png", "jpg"])#st.text_input('Enter full path of your profile image')
                        upload_new = st.button('Upload')
                        if upload_new:
                            uid = user['localId']
                            # Stored Initated Bucket in Firebase
                            fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                            # Get the url for easy access
                            a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                            # Put it in our real time database
                            db.child(user['localId']).child("Image").push(a_imgdata_url)
        # HOME PAGE
                elif bio == 'Home':
                #     col1, col2 = st.columns(2)
                    
                    #col1 for Profile picture
                    #with col1:
                    nImage = db.child(user['localId']).child("Image").get().val()         
                    if nImage is not None:
                        val = db.child(user['localId']).child("Image").get()
                        for img in val.each():
                            img_choice = img.val()
                        st.image(img_choice,width=300,caption='Profile Image')
                    else:
                        st.info("No profile picture yet. Go to Edit Profile and choose one!")
                            
                    post = st.text_input("Let's share my current mood as a post!",max_chars = 100)
                    add_post = st.button('Share Posts')
                    if add_post:   
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")              
                        post = {'Post:' : post,
                                    'Timestamp' : dt_string}                           
                        results = db.child(user['localId']).child("Posts").push(post)
                        st.balloons()

                        #This coloumn for the post Display
                #     with col2:
                        
                    all_posts = db.child(user['localId']).child("Posts").get()
                    if all_posts.val() is not None:    
                        for Posts in reversed(all_posts.each()):
                                #st.write(Posts.key()) # Morty
                                st.code(Posts.val(),language = '') 
        # WORKPLACE FEED PAGE
                else:
                    all_users = db.get()
                    res = []
                    # Store all the users handle name
                    for users_handle in all_users.each():
                        try:
                            k = users_handle.val()["Handle"]
                            res.append(k)
                        except:
                            st.write("Key Error")
                    # Total users
                    nl = len(res)
                    st.write('Total users here: '+ str(nl)) 
                    
                    # Allow the user to choose which other user he/she wants to see 
                    choice = st.selectbox('My Collegues',res)
                    push = st.button('Show Profile')
                    
                    # Show the choosen Profile
                    if push:
                        for users_handle in all_users.each():
                            try:
                                k = users_handle.val()["Handle"]
                            except:
                                st.write("key error")
                            if k == choice:
                                lid = users_handle.val()["ID"]
                                
                                handlename = db.child(lid).child("Handle").get().val()             
                                
                                st.markdown(handlename, unsafe_allow_html=True)
                                
                                nImage = db.child(lid).child("Image").get().val()
                                         
                                if nImage is not None:
                                    valu = db.child(lid).child("Image").get()
                                    for img in valu.each():
                                        img_choice = img.val()
                                        st.image(img_choice, width=250)
                                else:
                                    st.info("No profile picture yet. Go to Edit Profile and choose one!")
        
                                # All posts
                                all_posts = db.child(lid).child("Posts").get()
                                if all_posts.val() is not None:    
                                    for Posts in reversed(all_posts.each()):
                                        st.code(Posts.val(),language = '')
                    



