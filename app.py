from hugchat import hugchat


# Create a chatbot connection
chatbot = hugchat.ChatBot(cookie_path="cookies.json")

# New a conversation (ignore error)
id = chatbot.new_conversation()
chatbot.change_conversation(id)

uinput = input("Enter your message: ")

print(chatbot.chat(uinput))
