FROM python:2.7-slim

RUN mkdir -p /app
COPY . /app
WORKDIR /app

EXPOSE 5000

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libmysqlclient-dev

RUN pip install .

ENTRYPOINT ["python"]
CMD ["invoicer/application.py"]
