CREATE SCHEMA chesterton;

CREATE TABLE chesterton.users (
    id BIGINT PRIMARY KEY,
    email TEXT NOT NULL UNIQUE
);

INSERT INTO ops (op) VALUES ('migration V0001__initial_schema_chesterton.sql');
