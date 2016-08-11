from twilio.rest import TwilioRestClient

account_id="AC0b5fcd7d74dd53ca55a8c57324c35104"
auth="ebeb71c5d7d3e55571b09039960c543b"
client=TwilioRestClient(account_id,auth)

message=client.sms.messages.create(
    body="Holly, Shit! you won power ball to claim your money call 98480 2233",
    to="+15104035xx",
    from_="+13476583xxx")


print(message.sid)