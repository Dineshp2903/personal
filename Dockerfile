FROM debian:buster-slim


WORKDIR /app
COPY . /app



RUN apt-get update &&\
    apt-get install -y python3-pip


RUN pip3 install -r requirements.txt


CMD ["python", "main"]

