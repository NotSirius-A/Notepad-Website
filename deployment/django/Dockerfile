FROM python:3.13-slim

WORKDIR /my_app

COPY ./deployment/django/requirements.txt ./

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r ./requirements.txt


COPY ./src/ ./src/

EXPOSE 8000

COPY ./deployment/django/entry_point.sh ./
ENTRYPOINT ["sh", "./entry_point.sh"]