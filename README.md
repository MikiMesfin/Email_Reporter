# Email Reporter

An automated email reporting system that processes data and sends scheduled reports via email with optional SMS notifications.

## Features

- Automated daily email reports
- Data processing from CSV and Excel files
- SMS notifications for errors using Twilio
- Configurable schedule
- Customizable report templates
- HTML formatted email reports
- Error handling and logging

## Project Structure

```
email_reporter/
├── src/
│   ├── __init__.py
│   ├── email_sender.py
│   ├── sms_sender.py
│   └── data_processor.py
├── main.py
├── requirements.txt
└── .env
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/MikiMesfin/Email_Reporter.git
cd Email_Reporter
```

2. Create and activate virtual environment:
```bash:README.md
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your credentials:
```README.md
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
RECIPIENT_EMAIL=recipient@example.com
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number
ALERT_PHONE_NUMBER=recipient_phone_number
```

Note: For Gmail, you'll need to use an App Password instead of your regular password. Generate one in your Google Account settings under Security > 2-Step Verification > App passwords.

5. Run the script:
```bash
python main.py
```

## Configuration

- Reports are scheduled to run daily at 9:00 AM by default
- Modify the schedule in `main.py` to change the timing
- Customize report template in `data_processor.py`
- Supports both CSV and Excel file formats
- Configure email templates and SMS alerts as needed

## Usage

1. Place your data file (CSV or Excel) in the appropriate location
2. Update the file path in `main.py`
3. Run the script
4. The system will:
   - Process the data file
   - Generate HTML reports
   - Send emails at scheduled times
   - Send SMS alerts if any errors occur

## Error Handling

- Failed email attempts trigger SMS notifications
- All errors are logged with timestamps
- Automatic retry mechanism for failed operations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License

## Author

Miki Mesfin