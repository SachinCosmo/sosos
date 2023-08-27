import requests
import os
import json
from bardapi import Bard

bardKey = os.environ.get('_BARD_API_KEY')



def bardChat(data):
    # Create a session object using the requests library
    session = requests.Session()
    
    # Set the headers for the session
    session.headers = {
                "Host": "bard.google.com",
                "X-Same-Domain": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Origin": "https://bard.google.com",
                "Referer": "https://bard.google.com/",
            }
    
    # Set the "__Secure-1PSID" cookie with the Bard API key
    session.cookies.set("__Secure-1PSID", bardKey) 
    
    # Create a Bard object with the session and a timeout of 30 seconds
    bard = Bard(token=bardKey, session=session, timeout=30)
    answer = bard.get_answer(data)['content']
    print(answer)
    
    return json.dumps({'message':answer,'action':'null'})

uinput = input("You: ")
print(f"Uoy: {bardChat(uinput)}")
    