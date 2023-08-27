import streamlit as st 
from streamlit_option_menu import option_menu


def homepage():
    st.write("Home")
    st.write("Welcome to the homepage")
    
    
def chat():
    st.write("Chat")
    st.write("Welcome to the chat page")
    
def invoke_document():
    st.write("Invoke Document")
    st.write("Welcome to the invoke document page")
    
def invoke_audio():
    st.write("Invoke Audio")
    st.write("Welcome to the invoke audio page")
    
def invoke_video():
    st.write("Invoke Video")
    st.write("Welcome to the invoke video page")
    
def invoke_image():
    st.write("Invoke Image")
    st.write("Welcome to the invoke image page")
    
def invoke_text():
    st.write("Invoke Text")
    st.write("Welcome to the invoke text page")
    



def dashboard():
    
    with st.sidebar:
        selected = option_menu(None, ['Home', 'Chat', "Invoke Document", "Invoke Audio", "Invoke Video", "Invoke Image", "Invoke Text"],
                               icons=['🏠', '💬', "📄", "🔊", "🎥", "🖼️", "📝"])
        if selected == 'Home':
            homepage()
        elif selected == 'Chat':
            chat()
        elif selected == "Invoke Document":
            invoke_document()
        elif selected == "Invoke Audio":
            invoke_audio()
        elif selected == "Invoke Video":
            invoke_video()
        elif selected == "Invoke Image":
            invoke_image()
        elif selected == "Invoke Text":
            invoke_text()
        