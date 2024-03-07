import streamlit as st
import mysql.connector

def user1():
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
    def signup():
        username = st.text_input("Username",key ='sql')
        password = st.text_input("Password", type='password',key ='sqlp')

        if st.button("Sign Up"):
            insert_query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            cursor.execute(insert_query)
            conn.commit()
            st.success("Signup Successful!")


    def login():
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        
        if st.button("Login"):
            select_query = f"SELECT * FROM users WHERE username='{username}' and password='{password}'"
            cursor.execute(select_query)
            result = cursor.fetchone()
            if result:
                
                st.success("Login Successful!")
                st.session_state['logged'] = True
                
            else:
                st.error("Wrong username or password")
        
        

    # Show the login/signup form
    # st.set_page_config(page_title="Login/Sign Up", page_icon=":guardsman:", layout="wide")

    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Login":
        login()
    else:
        signup()

    # Close the database connection
    conn.close()
