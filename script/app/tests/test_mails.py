import pytest
import os
import sys

app_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(app_dir)
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

@pytest.mark.flask_app
def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.flask_app
def test_save_emails(client):
    data = {
        'event_id': '1000001',
        'email_subject': 'Test Subject',
        'email_content': 'Test Content',
        'timestamp': '27 Jun 2023 11:00'
    }
    response = client.post('/save_emails', data=data)
    assert response.status_code == 200
    assert b"Email saved successfully" in response.data

if __name__ == '__main__':
    pytest.main()