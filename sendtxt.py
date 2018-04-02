from twilio.rest import TwilioRestClient

account_sid ="AC820d5c804eed7b1c87b70e8af40ce4d0"
auth_token ="634303f3259d124f17cc19b1c5cb0013"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Hey....This is trial for msg using python.",
    to="+919993476418",
    from_="+12067454564")
print (message.sid)
