FROM debian:buster-slim

RUN apt-get update &&\
    apt-get install -y python3-pip