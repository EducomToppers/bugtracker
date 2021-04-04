FROM python:3.9.2-alpine3.13
WORKDIR /app
COPY ./requirements.txt .
COPY ./application .
RUN apk update \
    && apk add postgresql-client postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt

