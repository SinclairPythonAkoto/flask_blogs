"""This is a small unit test for the backend"""
import os
import pytest
import requests
from backend.app import Blog, Session, get_post, app

# Create an instance and save it to db
@pytest.fixture
def test_blog():
    session = Session()
    test_blog = Blog(title='Test Title', content='Test Content')
    session.add(test_blog)
    session.commit()
    yield test_blog
    session.delete(test_blog)
    session.commit()

@pytest.fixture
def test_blog2():
    session = Session()
    test_blog2 = Blog(title='Test Blog 2', content='Test Content 2')
    session.add(test_blog2)
    session.commit()
    yield test_blog2
    session.delete(test_blog2)
    session.commit()


# check if the data is stored in db
def test_get_db_blog_(test_blog):
    session = Session()
    post = session.query(Blog).filter_by(id=test_blog.id).first()
    assert post.title == 'Test Title'
    assert post.content == 'Test Content'


# check if the routing is correct
def test_blog_request(test_blog):
    # Get a new MapAdapter instance. For testing purpose, an empty string is fine
    # for the server name.
    adapter = app.url_map.bind('')
    # No exception occurs when there is a match..
    assert adapter.match(f'/post/{test_blog.id}')


def test_get_requests(test_blog):
    """This tests against the /post route on the Docker port.
    The first entry will need to be manually entered on docker web app 1st,
    then run the pytest for test to work.
    """
    res = requests.get(f'http://localhost:3304/post/{test_blog.id}')
    assert res.status_code == 200
    assert res.json()['title'] == test_blog.title
    assert res.json()['content'] == test_blog.content

