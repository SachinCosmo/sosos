import streamlit as st
from streamlit_option_menu import option_menu
import json
from Home import dashboard

import os
import pymongo
from pymongo.mongo_client import MongoClient



st.set_page_config(page_title="Auth", page_icon=":lock:") 

hide = """
<style>
footer {visibility: hidden;}
</style>
"""

st.markdown(hide, unsafe_allow_html=True)




uri = os.environ("MONGO_CONNECTION_STRING")

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


  
db = client['Cosmo']

col = db['Users']

newuser = {
    "username": "username",
    "password": "password",
}


col.insert_one(newuser)

def login():
    st.write("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in col.find():
            if password in col.find():
                st.session_state.user = username
                st.experimental_rerun()
            else:
                st.error("Incorrect password")
            
            
def register():
    st.write("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    newuser = {
    "username": username,
    "password": password,
}
    if st.button("Register"):
        col.insert_one(newuser)
        if username in col.find():
            st.error("User already exists")
        else:
            col.insert_one({"username": username, "password": password})
            st.success("User created")




def main():
    if 'user' not in st.session_state:
        st.session_state.user = None
        
    if st.session_state.user is None:
        with st.sidebar:
            selected = option_menu(None, ['Login', 'Register'])
        if selected == 'Login':
            login()
        elif selected == 'Register':
            register()
    else:
        dashboard()


if __name__ == "__main__":
    main()
