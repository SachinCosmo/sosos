from hugchat import hugchat
chatbot = hugchat.ChatBot(cookie_path="cookies.json")
print(chatbot.chat("Hi"))
# Create a new conversation
id = chatbot.new_conversation()
chatbot.change_conversation(id)
# Get conversation list
conversation_list = chatbot.get_conversation_list()
print(chatbot.chat("what is the most important thing to know as a human"))