FROM python:2.7

LABEL maintainer="Pedro"
RUN mkdir -p /app
COPY . /app
WORKDIR /app

EXPOSE 5000

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /invoicer

COPY . /bin

RUN pip install -r requirements.txt
WORKDIR /invoicer
RUN pip install flask-sqlalchemy
ENTRYPOINT ["python"]
CMD ["bin/invoicer-populatedb.py"]
CMD ["invoicer/application.py"]
