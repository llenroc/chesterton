CREATE TABLE rh_accounts (
    cid SERIAL PRIMARY KEY,
    id VARCHAR(20),
    data JSON,
    UNIQUE(id)
);

INSERT INTO ops (op) VALUES ('migration V0004__create_rh_accounts_table.sql');
