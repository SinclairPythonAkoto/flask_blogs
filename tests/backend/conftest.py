import pytest
from flask import Flask
from backend.app import app

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client