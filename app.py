from hugchat import hugchat
import streamlit as st

cookie_path = 'cookies.json'
chatbot = hugchat.ChatBot(cookie_path=cookie_path)

response = chatbot.start_conversation('Hello!')
print(response)

# chatbot = hugchat.ChatBot(cookie_path="home/user/cookies.json")
# with st.chat_message:
#     st.markdown(chatbot.chat("Hi"))
    
# # Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# # Get conversation list
# conversation_list = chatbot.get_conversation_list()
# uinput = st.chat_input("How can I help you?")
# with st.chat_message:
#     st.markdown(chatbot.chat(uinput))
    