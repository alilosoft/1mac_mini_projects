from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0cb4605072b26c735f51947dd6245815"
# Your Auth Token from twilio.com/console
auth_token  = "23a9b4287f3264b6bf7cd9e274603094"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+213779074707",
    from_="+18602001961",
    body="Hi alilo, You have to finish the 1MAC course!")

print(message.sid)
