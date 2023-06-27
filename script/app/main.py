import os
import pytz
import threading
from flask import Flask, request, render_template
from flask_mail import Mail, Message
from datetime import datetime, timedelta
from models import db, Email, Recipient
from config import Config

app = Flask(__name__)

# Configure the application
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

if app.config['FLASK_ENV'] != "PRODUCTION":
    app.debug = True


@app.route('/', methods=['GET'])
def main_page():
    emails = Email.query.all()
    recipients = Recipient.query.all()
    
    return render_template('index.html', saved_emails=emails, recipients=recipients)


@app.route('/save_emails', methods=['POST'])
def save_emails():
    # Extract the data from the request
    event_id = request.form.get('event_id')
    email_subject = request.form.get('email_subject')
    email_content = request.form.get('email_content')
    timestamp_str = request.form.get('timestamp')

    # Convert the timestamp to a datetime object
    timestamp = datetime.strptime(timestamp_str, '%d %b %Y %H:%M')
    # Adjust the timestamp to UTC+8 (Asia/Singapore)
    timezone = pytz.timezone('Asia/Singapore')
    timestamp = timezone.localize(timestamp)
    # Save the email to the database
    email = Email(event_id, email_subject, email_content, timestamp)
    db.session.add(email)
    db.session.commit()
    return 'Email saved successfully.'


def send_emails():
    with app.app_context():
        # Get the current time in UTC+8 (Asia/Singapore)
        current_time = datetime.now(pytz.timezone('Asia/Singapore'))
        # print(current_time)
        # Retrieve the emails that should be sent
        emails = Email.query.filter(Email.timestamp <= current_time).all()

        for email in emails:
            # Send the email
            # Replace the placeholders with the actual implementation to send the email
            try:
                print(email.timestamp)
                send_email(email.email_subject,
                           email.email_content)
                # Remove the email from the database
                db.session.delete(email)
                db.session.commit()
            except Exception as err:
                print(err)


def send_email(subject, content):
    # If environment is PRODUCTION, send actual email, otherwise only printf
    if app.config['FLASK_ENV'] == "PRODUCTION":
        # Create a message object
        subject = subject
        sender = app.config['MAIL_USERNAME']

        recipients = []
        # Retrieve the emails address on recipient table
        address = Recipient.query.all()
        for email in address:
            recipients.append(email.email_address)
        body = content
        message = Message(subject=subject, sender=sender,
                            recipients=recipients, body=body)
        mail = Mail(app)
        # Send the email
        mail.send(message)
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
    app.run(host='0.0.0.0', port=5000)
