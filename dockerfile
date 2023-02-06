FROM alpine:latest
RUN apk update
RUN apk add python3 py3-pip
RUN apk add py3-beautifulsoup4
RUN apk add py3-requests

RUN mkdir app
COPY Scraper.py app/Scraper.py
WORKDIR /app

ENTRYPOINT [ "python3", "Scraper.py" ]