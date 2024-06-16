"""
Tests for the Flask application.
"""

import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Example CI/CD Pipeline App' in response.data

def test_health(client):
    """Test the health endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'UP'}

def test_status(client):
    """Test the status endpoint."""
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json == {
        'service': 'Example CI/CD Pipeline',
        'status': 'Running',
        'version': '1.0'
    }
