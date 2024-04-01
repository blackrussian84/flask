# test_app.py
import pytest
import requests
from app import app, post_counter

# Unit test
def test_health_check():
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert response.data == b'OK'

# Integration test
def test_counter_get():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'0' in response.data  # Assuming the counter starts at 0

def test_counter_post():
    global post_counter
    initial_counter = post_counter
    with app.test_client() as client:
        response = client.post('/')
    assert response.status_code == 200
    # Add any other assertions you need here    