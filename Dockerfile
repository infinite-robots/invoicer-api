FROM python:2.7

LABEL maintainer="Pedro"
RUN mkdir -p /app
COPY . /app
WORKDIR /app

EXPOSE 5000

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN ls
COPY . /invoicer

WORKDIR invoicer
RUN ls
RUN pip install -r requirements.txt
RUN ls
#RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["application.py"]
