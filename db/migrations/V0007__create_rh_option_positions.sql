CREATE TABLE rh_option_positions (
    cid BIGINT PRIMARY KEY,
    id VARCHAR(36),
    chain_id VARCHAR(36),
    option VARCHAR(255),
    url VARCHAR(255),
    average_price NUMERIC(8,2),
    trade_value_multiplier NUMERIC(8,2),
    chain_symbol VARCHAR(20),
    strike_price NUMERIC(10,4),
    expiration_date DATE,
    type VARCHAR(20),
    option_type VARCHAR(20),
    quantity NUMERIC(8,2)
);

INSERT INTO ops (op) VALUES ('migration V0001__initial_schema_chesterton.sql');
