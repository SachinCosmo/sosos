import streamlit as st
import json

st.set_page_config(page_title="Reminder App", page_icon=":bell:", layout="centered")

login, signup = st.tabs(["Login", "Signup"])


@st.cache_data
def loadFile():
    with open("database/test.json") as json_file:
       return  json.load(json_file)
        
    
def saveFile(data):
    with open("database/test.json", "w") as file:
        json.dump(data, file, indent=4)

def LoginPage():
    st.title("Login")
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    if st.button("Login"):
        data = loadFile()
        for user in data["users"]:
            if username == user["username"] and password == user["password"]:
                st.success("Logged in as {}".format(username))
                st.balloons()  
            else:
                st.error("Incorrect username or password")
            
def SignupPage():
    st.title("Signup")
    username = st.text_input("Username", key="svusername")
    email = st.text_input("Email", key="svemail")
    password = st.text_input("Password", type="password", key="svpassword")
    if st.button("Signup"):
        data = loadFile()
        data["users"].append({"username": username, "password": password, "email": email})
        saveFile(data)
        st.success("Successfully signed up as {}".format(username))
            
with login:
    LoginPage()
    
with signup:
    SignupPage()




