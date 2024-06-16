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

def test_hello_world(client):
    """Test the hello_world endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, CI/CD!'}

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
