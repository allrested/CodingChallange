FROM python:3.9-slim

WORKDIR /app

LABEL maintainer="Tatsuya <allrested@gmail.com>"

RUN apt-get update \
    && apt-get -y install nano

COPY requirements.txt /tmp/requirements.txt

EXPOSE 5000

RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["python", "main.py"]