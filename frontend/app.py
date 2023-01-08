from flask import Flask, render_template

app = Flask(__name__)

# config your host & port for app
HOST = "0.0.0.0"
PORT = 5003


# define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create_blog.html')


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)