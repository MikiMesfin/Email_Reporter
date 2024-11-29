from twilio.rest import Client
import os
from dotenv import load_dotenv

class SMSSender:
    def __init__(self):
        load_dotenv()
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_number = os.getenv('TWILIO_PHONE_NUMBER')
        self.client = Client(self.account_sid, self.auth_token)

    def send_alert(self, to_number: str, message: str):
        """
        Send SMS alert
        """
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            return True
        except Exception as e:
            print(f"Failed to send SMS: {str(e)}")
            return False
