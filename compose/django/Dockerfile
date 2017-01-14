FROM python:3.5
MAINTAINER Nash <nashruddin.amin@gmail.com>

ADD . /app
ADD ./compose/django/server.sh /server.sh

RUN chmod +x /server.sh && \
    cd /app && \
    apt-get update && \
    pip install -r requirements.txt

WORKDIR /app
CMD ["/server.sh"]