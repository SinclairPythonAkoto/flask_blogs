from flask import Flask, request, jsonify, render_template, url_for, redirect
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

# config your host & port for app
HOST = "0.0.0.0"
PORT = 5004

# config db
engine = create_engine('sqlite:///blog.db')
Base = declarative_base()

class Blog(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# backend for creating a new blog
@app.route('/create_blog', methods=['POST'])    # the route name CANNOT be the same as the frontend
def create_blog():
    # Get the data for the new post from the request
    title = request.form['title']
    content = request.form['content']

    # Create a new post object
    post = Blog(title=title, content=content)

    # Add the post to the database
    session.add(post)
    session.commit()

    success = 'New blog created successfully!'

    return render_template('index.html', success=success)


# backend api
@app.route('/post/<int:post_id>')
def get_post(post_id):
    # get a specific post
    post = session.query(Blog).filter_by(id=post_id).first()
    res = {
        'id': post.id,
        'title': post.title,
        'content': post.content
    }
    return jsonify(res)


@app.route('/posts')
def get_posts():
    # Fetch all posts from the database
    posts = session.query(Blog).all()

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