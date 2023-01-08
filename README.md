This is a simple Flak blog app within a monolithic structure deployed from a docker container.

The Flask port for this app is set to 5002 while the port for the docker is 81.

This means that to run the app on my local machine I use 127.0.0.1:5002 and to run the app with Docker I use 127.0.0.1:81.

### Run on local machine
```
python app.py

# navigate to the web browser
127.0.0.1:5002

# create a blog post
127.0.0.1:5002/create

# view all blogs
127.0.0.1:5002/posts
```

### Run in container
```
# build your docker image
docker build -t hello_world .

# build & deploy app using docker-compose.yml file
docker-compose up -d

# remove docker 
docker-compose down

# navigate to the web browser
127.0.0.1:81

# create a blog post
127.0.0.1:81/create

# view all blogs
127.0.0.1:81/posts
```