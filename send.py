from twilio.rest import Client

account_sid = 'AC76f19c0915cb9247e38639f9bb55f1b6'
auth_token = '1de0bddded12e5be293e2c2b3a4b44b4'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
        from_='+13257488617',
        body='Alert!!',
        to='+918767871973'
        )
    
    print(message.sid)