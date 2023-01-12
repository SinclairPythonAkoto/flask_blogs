# Flask Blog - Microservices

This is a simple Flak blog app within a microservices structure deployed from a docker container.
It also contains unit tests being run to check the application process.

To run the Pytest run:
```
python -m pytest tests/...
```

For this is, the `python -m pytest` is needed becuase of how the Flask apps are set up in a modular fashion.

This app has a frontend and a backend which are both separate Flask apps, which use the same VE.
In the future the VE should be set up within each app directory.