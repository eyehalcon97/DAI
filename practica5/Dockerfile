# Dockerfile
FROM python:3.9-alpine
WORKDIR /app  
COPY . /app
RUN apk add gcc musl-dev jpeg-dev zlib-dev python3-dev libffi-dev openssl-dev cargo \
    && pip install -r requirements.txt

