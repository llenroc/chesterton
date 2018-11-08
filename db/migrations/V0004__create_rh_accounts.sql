CREATE TABLE rh_accounts (
    cid BIGINT PRIMARY KEY,
    id VARCHAR(20),
    data json
);

INSERT INTO ops (op) VALUES ('migration V0004__create_rh_accounts_table.sql');
