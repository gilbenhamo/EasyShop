FROM python:3.7.0

RUN python3 -m pip install --upgrade pip

WORKDIR /code/
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . /code/
