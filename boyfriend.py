from twilio.rest import Client
import random 
 
account_sid = 'ACbf8c97ce07c86f7b8033f6ea64b59d4d' 
auth_token = '1b1c07cd85f39e4a771a3f7cc89dcf8c' 
client = Client(account_sid, auth_token) 
messages = ["I love you","You are really beautiful","One day you will find someone","Try your best babygirl"]

def send_message():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body= print(random.choice(messages)),
                              to='whatsapp:+919643882723' 
                            ) 
 
    print(message.sid)