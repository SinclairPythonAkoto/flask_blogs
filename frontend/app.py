from flask import Flask

app = Flask(__name__)

# config your host & port for app
HOST = "0.0.0.0"
PORT = 5003


# define routes
@app.route('/')
def home():
    return 'Welcome to the blog!'


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)