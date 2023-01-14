# Flask Blog - Microservices

This is a simple Flak blog app within a microservices structure deployed from a docker container.
In this app I will create a Continuous Intergeration & Continuous Development process to automate my testing.

This web app contains two Flask apps - for the frontend and backend, with a CI/CD pipeline to run
tests on the frontend & backend.  Because I am testing the Flask apps within the docker containers, 
they some tests are regression tests. The pull request will not be successful if the tests fail.

To run the Pytest run:
```
python -m pytest tests/...
```
For this is, the `python -m pytest` is needed becuase of how the Flask apps are set up in a modular fashion.


To run app in docker:
```
docker-compose up -d --build
```

Navigate to frontend:
```
# create a new blog
http://localhost:3303/create
```

Navigate to backend:
```
# find blog by id
http://localhost:3304/post/1

# find all blogs
http://localhost:3304/posts
```

The first blog entry should be named `Test Title` and the content should contain `Test Content`. 
This is used for the pytest. After that you can create any any blog you wish (as is it won't be applied in the 
unit tests).
