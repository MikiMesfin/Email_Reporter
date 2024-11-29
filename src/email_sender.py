import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

class EmailSender:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv('EMAIL_ADDRESS')
        self.password = os.getenv('EMAIL_PASSWORD')
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))

    def send_report(self, to_email: str, subject: str, body: str, attachments: list = None):
        """
        Send email with optional attachments
        """
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add body
        msg.attach(MIMEText(body, 'html'))

        # Add attachments if any
        if attachments:
            for file in attachments:
                with open(file, 'rb') as f:
                    attachment = MIMEApplication(f.read(), _subtype='pdf')
                    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                    msg.attach(attachment)

        # Send email
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False
