from twilio.rest import Client 
 
account_sid = 'ACbf8c97ce07c86f7b8033f6ea64b59d4d' 
auth_token = '1b1c07cd85f39e4a771a3f7cc89dcf8c' 
client = Client(account_sid, auth_token) 
def send_message():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hello mom ',      
                              to='whatsapp:+919811522307' 
                          ) 
 
    print(message.sid)