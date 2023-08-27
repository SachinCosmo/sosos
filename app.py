from hugchat import hugchat
import streamlit as st

chatbot = hugchat.ChatBot(cookie_path="cookies.json")
with st.chat_message:
    st.markdown(chatbot.chat("Hi"))
    
# # Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# # Get conversation list
# conversation_list = chatbot.get_conversation_list()
# uinput = st.chat_input("How can I help you?")
# with st.chat_message:
#     st.markdown(chatbot.chat(uinput))
    