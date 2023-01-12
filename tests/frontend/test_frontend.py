import pytest
from flask import Flask
from frontend import app

@pytest.fixture
def app():
    app = app
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to my Blog' in response.data


def test_create_blog(client):
    response = client.post('/create', data={'title': 'Test Title', 'content': 'Test Content'})
    assert response.status_code == 200