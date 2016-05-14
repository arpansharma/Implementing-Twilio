from twilio.rest import TwilioRestClient

account_sid = "{{ account_sid }}" # Your Account SID from www.twilio.com/console
auth_token = "{{ auth_token }}" # Your Auth Token from www.twilio.com/console

twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '# Replace with your Twilio number'
myCellPhone = '# Replace with your phone number'

message = twilioCli.messages.create(body='Your message')

print "SMS Sent !"
