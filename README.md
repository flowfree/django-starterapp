Django Starter App
==================

[![Build Status](https://travis-ci.org/flowfree/django-starterapp.svg?branch=master)](https://travis-ci.org/flowfree/django-starterapp)

A starter app for my Django projects.

Run On Development Machine
--------------------------

1.  Create new virtualenv:

        python3 -m venv venv
        . venv/bin/activate

2.  Install package dependencies:

        pip install -r requirements.txt

3.  Create new PostgreSQL database and user:

        CREATE DATABASE dbname;
        CREATE USER dbuser WITH PASSWORD 's3cr3t';
        ALTER ROLE dbuser SET client_encoding TO 'utf8';
        ALTER ROLE dbuser SET default_transaction_isolation TO 'read committed';
        ALTER ROLE dbuser SET timezone TO 'UTC';
        ALTER USER dbuser CREATEDB;
        GRANT ALL PRIVILEGES ON DATABASE dbname TO dbuser;

4.  Create new `.env` file:

        cp .env.example .env

5.  Fill in the values for PostgreSQL and leave the others empty:

        POSTGRES_DBNAME=dbname
        POSTGRES_USER=dbuser
        POSTGRES_PASSWORD=s3cr3t

6.  Run the development server:

        ./manage.py migrate
        ./manage.py runserver 3000

Deploy on Dedicated Server
--------------------------

Make sure that you have [Docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

1.  Create new `.env` file:

        cp .env.example .env

2.  Fill in all of the values.

3.  Build and run the containers:

        docker-compose build && docker-compose up -d


Deploy on Heroku
----------------

Make sure you have [Heroku CLI](https://cli.heroku.com/) installed on your computer.

1.  Login to Heroku:

        heroku login

2.  Create new Heroku app:

        heroku create

3.  Set the environment variables:

        heroku config:set DJANGO_SETTINGS_MODULE=config.settings.heroku
        heroku config:set DJANGO_SECRET_KEY=<value>

4.  Push code:

        git push heroku master

5.  Run database migrations and optionally create a user:

        heroku run ./manage.py migrate

6.  Open the app:

        heroku open


TODO
----

- Custom error pages for 4xx and 5xx
- HTML email
    