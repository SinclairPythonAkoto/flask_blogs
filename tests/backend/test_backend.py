import pytest
from flask import Flask
from backend.app import Blog, Session

@pytest.fixture
def test_blog():
    session = Session()
    test_blog = Blog(title='Test Title', content='Test Content')
    session.add(test_blog)
    session.commit()
    yield test_blog
    session.delete(test_blog)
    session.commit()

def test_get_post(client, test_blog):
    response = client.get(f'/post/{test_blog.id}')
    assert response.status_code == 200
    assert response.json['title'] == 'Test Title'
    assert response.json['content'] == 'Test Content'
