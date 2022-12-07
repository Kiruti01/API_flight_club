from twilio.rest import Client

TWILIO_SID = "AC1f598b94a05236d62dfc7ce761bb6f1b"
TWILIO_AUTH_TOKEN = "3c582b6e93b7906534fe7298eb86dab1"
TWILIO_VIRTUAL_NUMBER = "+19897689210"
TWILIO_VERIFIED_NUMBER = "+254716542844"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


    # def send_emails(self, emails, message, google_flight_link):
    #     with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         for email in emails:
    #             connection.sendmail(
    #                 from_addr=MY_EMAIL,
    #                 to_addrs=email,
    #                 msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
    #             )