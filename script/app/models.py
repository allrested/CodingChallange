from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Email(db.Model):
    __tablename__ = 'email'
    # Defined of table columns
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    email_subject = db.Column(db.String(100))
    email_content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)

    def __init__(self, event_id, email_subject, email_content, timestamp):
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.timestamp = timestamp

class Recipient(db.Model):
    __tablename__ = 'recipient'
    # Defined of table columns
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.Text)

    def __init__(self, email_address):
        self.email_address = email_address
