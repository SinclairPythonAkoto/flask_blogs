from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# config your host & port for app
HOST = "0.0.0.0"
PORT = 5004

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

@app.route('/post', methods=['POST'])
def create_post():
    # create a new post
    new_post = Blog(title=request.form['title'], content=request.form['content'])
    db.session.add(new_post)
    db.session.commit()
    return 'Success'

@app.route('/post/<int:post_id>')
def get_post(post_id):
    # get a specific post
    post = Blog.query.get(post_id)
    return post.title

# backend api
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