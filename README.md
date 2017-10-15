Django Starter App
==================

[![Build Status](https://travis-ci.org/flowfree/django-starterapp.svg?branch=master)](https://travis-ci.org/flowfree/django-starterapp)

A starter app for my Django projects.

On Development Machine
----------------------

Create new PostgreSQL database and user:

    CREATE DATABASE dbname;
    CREATE USER dbuser WITH PASSWORD 's3cr3t';
    ALTER ROLE dbuser SET client_encoding TO 'utf8';
    ALTER ROLE dbuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE dbuser SET timezone TO 'UTC';
    ALTER USER dbuser CREATEDB;
    GRANT ALL PRIVILEGES ON DATABASE dbname TO dbuser;

Create new `.env` file:

    cp .env.example .env

Fill in the values for PostgreSQL and leave the others empty:

    POSTGRES_DBNAME=dbname
    POSTGRES_USER=dbuser
    POSTGRES_PASSWORD=s3cr3t

Create new virtualenv and install dependencies:

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Run the development server:

    ./manage.py migrate
    ./manage.py runserver 3000

On Production Server
--------------------

Create new `.env` file as above and fill in all of the values. Run docker-compose:

    docker-compose build
    docker-compose up -d

TODO
----

- Custom error pages for 4xx and 5xx
- HTML email
    