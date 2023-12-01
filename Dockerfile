# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

LABEL autor="Michal Goryszewski"
LABEL version="1.0.1"

WORKDIR /app

COPY ["req.txt" ,"./"]

RUN pip3 install -r req.txt

COPY . .
EXPOSE 5000
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD [ "python3" ,"-m" ,"flask" , "run" ]