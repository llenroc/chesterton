CREATE TABLE option_groupings (
    cid BIGINT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO ops (op) VALUES ('migration V0001__initial_schema_chesterton.sql');
