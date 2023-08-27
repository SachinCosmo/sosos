from hugchat import hugchat
from hugchat.login import Login
import streamlit as st 

# Log in to huggingface and grant authorization to huggingchat
sign = Login(mecosmo369@gmail.com, @_3SegZXGjrjff/)
cookies = sign.login()

# Save cookies to the local directory
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
print(chatbot.chat("Hi!"))

# Create a new conversation
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# Get conversation list
conversation_list = chatbot.get_conversation_list()
if uinput := st.chat_input("How can I help you?"):
    with st.chat_message:
        st.markdown(chatbot.chat(uinput))
    

# # Switch model (default: meta-llama/Llama-2-70b-chat-hf. )
# chatbot.switch_llm(0) # Switch to `OpenAssistant/oasst-sft-6-llama-30b-xor`
# chatbot.switch_llm(1) # Switch to `meta-llama/Llama-2-70b-chat-hf`


