FROM python:3.10-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
RUN pip install swagger-ui-py

EXPOSE 5002

CMD ["python", "app.py"]