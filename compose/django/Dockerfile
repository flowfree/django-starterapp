FROM python:3.5
MAINTAINER Nash <nashruddin.amin@gmail.com>

ENV DJANGO_SETTINGS_MODULE config.settings.production

ADD . /app
ADD ./compose/django/server.sh /server.sh

RUN chmod +x /server.sh && \
    cd /app && \
    apt-get update && \
    pip install -r requirements.txt

WORKDIR /app
CMD ["/server.sh"]