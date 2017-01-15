Django Starter App
==================

A starter app for my Django projects, inspired by [Cookiecutter Django](https://cookiecutter-django.readthedocs.io/en/latest/).

On Development Machine
----------------------

Create new PostgreSQL database and user:

    CREATE DATABASE dbname;
    CREATE USER dbname WITH PASSWORD 's3cr3t';
    ALTER ROLE dbname SET client_encoding TO 'utf8';
    ALTER ROLE dbname SET default_transaction_isolation TO 'read committed';
    ALTER ROLE dbname SET timezone TO 'UTC';
    ALTER USER dbname CREATEDB;
    GRANT ALL PRIVILEGES ON DATABASE dbname TO dbname;

Create new `.env` file:

    cp .env.example .env

Fill in the values for PostgreSQL and leave the others empty:

    POSTGRES_USER=dbname
    POSTGRES_PASSWORD=s3cr3t

Create new virtualenv and install dependencies:

    pyvenv venv
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
    