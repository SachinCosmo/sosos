import streamlit as st
from streamlit_option_menu import option_menu
import json
from Home import dashboard
import pymongo


st.page_config(page_title="Auth", page_icon=":lock:")




def loadfile():
    with open("database/users.json") as file:
        data = json.load(file)
    return data

def savefile(data):
    with open("database/users.json", "w") as file: 
        json.dump(data, file, indent=4)



def login():
    st.write("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        data = loadfile()
        if username in data:
            if data[username]["password"] == password:
                st.success("Logged In as {}".format(username))
                st.session_state.user = username
            else:
                st.error("Wrong Password")
        else:
            st.error("User not found")
            
            
def register():
    st.write("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        data = loadfile()
        if username in data:
            st.error("User already exists")
        else:
            data[username] = {}
            data[username]["password"] = password
            savefile(data)
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