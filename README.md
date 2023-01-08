This is a quick Flask app displaying `Hello World`.

With this app the port for the Flask is set to `5001` while the port for the docker is `80`.

This means that to run the app on my local machine I use `127.0.0.1:5001` and to run the app with Docker I use `127.0.0.1:80`.

### Run on local machine
```
python app.py

# navigate to the web browser
127.0.0.1:500
```

### Run in container
```
# build your docker image
docker build -t hello_world .

# build & deploy app using docker-compose.yml file
docker-compose up -d

# remove docker 
docker-compose down
```