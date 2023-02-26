FROM debian:buster-slim



COPY requirements.txt .

RUN apt-get update &&\
    apt-get install -y python3-pip


RUN pip3 install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
