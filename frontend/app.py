from flask import Flask, render_template
import os
from dotenv import load_dotenv

app = Flask(__name__)

# set path for environment variables file
load_dotenv(dotenv_path='.env')

# config your host & port for app using environment variables
HOST = os.environ['HOST']
PORT = os.environ['FRONTEND_PORT']
<<<<<<< HEAD

=======
>>>>>>> a549a6f... remove error


# define routes
@app.route('/')
def home():
    return render_template('index.html')

# frontend for creating a new blog
@app.route('/create', methods=['GET'])
def create():
    return render_template('create_blog.html')


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)