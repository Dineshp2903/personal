FROM python:3.8


WORKDIR /app
COPY . /app



#RUN apt-get update &&\
#    apt-get install -y python3-pip


RUN pip3 install -r requirements.txt

EXPOSE 8080


CMD ["python3", "main.py"]

