from twilio.rest import Client


class SMSManager:
        # Your Account SID from twilio.com/console
    account_sid = "ACc63422cf9e6d38129b39a3cfb0be51cc"
    # Your Auth Token from twilio.com/console
    auth_token = "dce98c38437660974a9e5bd8c652a03b"

    def send_message(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            to="+12134482436",
            from_="+14248359366",
            body=message)
