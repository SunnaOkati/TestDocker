FROM python:3.9.13-slim-buster
ADD src/requirements.txt /src/
RUN apt-get update \
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r /src/requirements.txt \
    && apt-get purge -y --auto-remove gcc
