FROM ubuntu:18.04

RUN apt update && apt install -y \
    python3 python3-pip

RUN pip install --upgrade pip

WORKDIR /code/
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY * /code/