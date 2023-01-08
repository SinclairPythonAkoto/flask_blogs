from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from swagger_ui_py import Api, Operation


app = Flask(__name__)


# config your host & port for app
HOST = "0.0.0.0"
PORT = 5002


# config db
engine = create_engine('sqlite:///blog.db')
Base = declarative_base()


# create db models
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# add your routes
@app.route('/')
def home():
    return render_template('index.html')

# frontend for creating a blog
@app.route('/create')
def create_post_form():
    return render_template('create_post.html')

# backend for creating a blog
@app.route('/post', methods=['POST'])
def create_post():
    # Get the data for the new post from the request
    title = request.form['title']
    content = request.form['content']

    # Create a new post object
    post = Post(title=title, content=content)

    # Add the post to the database
    session.add(post)
    session.commit()

    return 'Post created successfully!'

# backend api
@app.route('/posts')
@Api(
    title='Blog API',
    version='1.0',
    description='A simple API for creating and retrieving blog posts',
)
@Operation(
    summary='Get all blog posts',
    description='Retrieves a list of all blog posts from the database',
    responses={
        200: {'description': 'Success'},
        500: {'description': 'Internal server error'},
    }
)
def get_posts():
    # Fetch all posts from the database
    posts = session.query(Post).all()

    # Convert the posts to a list of dictionaries
    post_list = []
    for post in posts:
        post_list.append({
            'id': post.id,
            'title': post.title,
            'content': post.content
        })

    return jsonify(post_list)




if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)