Create database
---------------
    CREATE DATABASE starterapp;
    CREATE USER starterapp WITH PASSWORD 's3cr3t';
    ALTER ROLE starterapp SET client_encoding TO 'utf8';
    ALTER ROLE starterapp SET default_transaction_isolation TO 'read committed';
    ALTER ROLE starterapp SET timezone TO 'UTC';
    ALTER USER starterapp CREATEDB;
    GRANT ALL PRIVILEGES ON DATABASE starterapp TO starterapp;
