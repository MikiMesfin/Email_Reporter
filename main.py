import schedule
import time
from src.email_sender import EmailSender
from src.sms_sender import SMSSender
from src.data_processor import DataProcessor
import os
from dotenv import load_dotenv
from datetime import datetime

def send_daily_report():
    print(f"Sending daily report at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    try:
        # Initialize components
        data_processor = DataProcessor('path/to/your/data.csv')
        email_sender = EmailSender()
        sms_sender = SMSSender()

        # Generate report
        report_html = data_processor.generate_report()

        # Send email
        success = email_sender.send_report(
            to_email=os.getenv('RECIPIENT_EMAIL'),
            subject='Daily Data Report',
            body=report_html
        )

        if success:
            print("Report sent successfully!")
        else:
            print("Failed to send report email.")
            # Send SMS notification
            sms_sender.send_alert(
                to_number=os.getenv('ALERT_PHONE_NUMBER'),
                message='Failed to send daily report email!'
            )

    except Exception as e:
        error_msg = f"Error in daily report: {str(e)}"
        print(error_msg)
        sms_sender.send_alert(
            to_number=os.getenv('ALERT_PHONE_NUMBER'),
            message=error_msg
        )

def main():
    load_dotenv()
    
    print(f"Email Reporter started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Scheduling daily report for 09:00 AM")
    
    # Schedule the report to run daily at 9:00 AM
    schedule.every().day.at("09:00").do(send_daily_report)
    
    # Option to run report immediately for testing
    user_input = input("Would you like to send a test report now? (y/n): ")
    if user_input.lower() == 'y':
        send_daily_report()
    
    print("\nWaiting for scheduled time... Press Ctrl+C to exit")
    print("Next report will be sent at 09:00 AM")
    
    # Run continuously
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
            # Print a status update every hour
            if datetime.now().minute == 0:
                print(f"Still running... Current time: {datetime.now().strftime('%H:%M')}")
    except KeyboardInterrupt:
        print("\nShutting down Email Reporter...")

if __name__ == "__main__":
    main()
