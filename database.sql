\c postgres

DROP DATABASE IF EXISTS takemethere;
CREATE DATABASE takemethere;
\c takemethere;
CREATE EXTENSION pgcrypto;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
                    email VARCHAR(32) NOT NULL,
                    PRIMARY KEY(email),
                    firstName VARCHAR(32) NOT NULL DEFAULT 'John',
                    lastName VARCHAR(32) NOT NULL DEFAULT 'Doe',
                    password VARCHAR(64) NOT NULL
                    );