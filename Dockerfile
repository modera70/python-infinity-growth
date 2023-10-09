FROM python:3.11.1-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /framework/src
COPY ./test /framework/test
COPY chrome-browser-config.json /framework/chrome-browser-config.json
COPY edge-browser-config.json /framework/edge-browser-config.json
COPY firefox-browser-config.json /framework/firefox-browser-config.json
COPY wait-for-grid.sh /framework/wait-for-grid.sh

RUN apt-get update
RUN apt-get -y install jq
RUN apt-get -y install curl
RUN chmod +x /framework/wait-for-grid.sh

WORKDIR /framework
ENV PYTHONPATH=/framework

ENTRYPOINT ./wait-for-grid.sh python -m pytest --alluredir=./tmp/allure-results
