# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACd6687526ddd249e5dd9a731ee20a05fc'
auth_token = '6f3a73235618d67768a97e4658b5acf5'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+17275132450',
                              body='Elephant Detected',
                              to='+919438017057'
                          )

print(message.sid)
