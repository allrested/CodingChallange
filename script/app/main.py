from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
import pytz
import threading
import mailtrap as mt

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] =  f"{os.getenv('SQLALCHEMY_DATABASE_URI')}"
app.config['MAILTRAP_API_KEY'] =  f"{os.getenv('MAILTRAP_API_KEY')}"
app.config['MAILTRAP_EMAIL_ADDRESS'] =  f"{os.getenv('MAILTRAP_EMAIL_ADDRESS')}"
app.config['MAILTRAP_EMAIL_NAME'] =  f"{os.getenv('MAILTRAP_EMAIL_NAME')}"
db = SQLAlchemy(app)

app.debug = True

# Define the Email model
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    email_subject = db.Column(db.String(100))
    email_content = db.Column(db.Text)
    email_address = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)

    def __init__(self, event_id, email_subject, email_content, email_address, timestamp):
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.email_address = email_address
        self.timestamp = timestamp

@app.route('/', methods=['GET'])
def main_page():
    return "Welcome"

@app.route('/save_emails', methods=['POST'])
def save_emails():
    # Extract the data from the request
    event_id = request.form.get('event_id')
    email_subject = request.form.get('email_subject')
    email_content = request.form.get('email_content')
    email_address = request.form.get('email_address')
    timestamp_str = request.form.get('timestamp')

    # Convert the timestamp to a datetime object
    timestamp = datetime.strptime(timestamp_str, '%d %b %Y %H:%M')
    # Adjust the timestamp to UTC+8 (Asia/Singapore)
    timezone = pytz.timezone('Asia/Singapore')
    timestamp = timezone.localize(timestamp)
    # Save the email to the database
    email = Email(event_id, email_subject, email_content, email_address, timestamp)
    db.session.add(email)
    db.session.commit()

    return 'Email saved successfully.'

def send_emails():
    with app.app_context():
        # Get the current time in UTC+8 (Asia/Singapore)
        current_time = datetime.now(pytz.timezone('Asia/Singapore'))

        # Retrieve the emails that should be sent
        emails = Email.query.filter(Email.timestamp <= current_time).all()

        for email in emails:
            # Send the email
            # Replace the placeholders with the actual implementation to send the email
            send_email(email.email_subject, email.email_content, email.email_address)

            # Remove the email from the database
            db.session.delete(email)
            db.session.commit()

def send_email(subject, content, address):
    # Replace this with the actual implementation to send the email
    # using a library like smtplib
    mail = mt.Mail(
        sender=mt.Address(email=app.config['MAILTRAP_EMAIL_ADDRESS'], name=app.config['MAILTRAP_EMAIL_NAME']),
        to=[mt.Address(email=address)],
        subject=subject,
        text=content,
        category="Integration Test",
    )

    client = mt.MailtrapClient(token=app.config['MAILTRAP_API_KEY'])
    client.send(mail)
    print(f'Sending email with subject: {subject}')
    print(f'Content: {content}')

def check_emails_periodically():
    while True:
        send_emails()
        # Sleep for 1 minute before checking again
        threading.Event().wait(60)

if __name__ == '__main__':
    # Start a separate thread to check and send emails periodically
    email_thread = threading.Thread(target=check_emails_periodically)
    email_thread.start()

     # Create the database directory if it doesn't exist
    db_directory = os.path.dirname(app.config['SQLALCHEMY_DATABASE_URI'])
    os.makedirs(db_directory, exist_ok=True)

    with app.app_context():
        # Create database tables
        db.create_all()

    # Run the Flask application
    app.run()