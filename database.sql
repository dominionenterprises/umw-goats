\c postgres

DROP DATABASE IF EXISTS takemethere;
CREATE DATABASE takemethere;
\c takemethere;
CREATE EXTENSION pgcrypto;

DROP TABLE IF EXISTS users;
CREATE TABLE users
(
    email VARCHAR(32) NOT NULL,
    PRIMARY KEY(email),
    firstName VARCHAR(32) NOT NULL DEFAULT 'John',
    lastName VARCHAR(32) NOT NULL DEFAULT 'Doe',
    password VARCHAR(64) NOT NULL
);

DROP TABLE IF EXISTS location;
CREATE TABLE location
(
    id SERIAL PRIMARY KEY,
    address VARCHAR(32) NOT NULL,
    city VARCHAR(32) NOT NULL,
    state VARCHAR(32) NOT NULL,
    zipcode VARCHAR(32) NOT NULL,
    state VARCHAR(32) NOT NULL,
    country VARCHAR(32) NOT NULL,
);

DROP TABLE IF EXISTS crime;
CREATE TABLE crime
(
    
);

DROP TABLE IF EXISTS traffic;
CREATE TABLE traffic
(
    
);

DROP TABLE IF EXISTS restauraunts;
CREATE TABLE restauraunts
(
    
);

DROP TABLE IF EXISTS shops;
CREATE TABLE shops
(
    
);

DROP TABLE IF EXISTS schools;
CREATE TABLE schools
(
    
);
