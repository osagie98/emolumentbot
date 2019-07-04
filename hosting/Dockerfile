FROM ubuntu:latest

RUN apt update
RUN apt install -y python python-pip
RUN apt install -y git
RUN git clone https://github.com/osagie98/emolumentbot.git

WORKDIR emolumentbot

RUN python -m pip install -r requirements.txt