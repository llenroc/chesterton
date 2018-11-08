CREATE TABLE rh_option_orders (
    cid SERIAL PRIMARY KEY,
    id VARCHAR(36),
    chain_id VARCHAR(36),
    chain_symbol VARCHAR(20),
    strike_price NUMERIC(10,4),
    expiration_date DATE,
    contract_type VARCHAR(20),
    side VARCHAR(20),
    option VARCHAR(255),
    state VARCHAR(20),
    direction VARCHAR(20),
    position_effect VARCHAR(20),
    ratio_quantity INTEGER,
    price NUMERIC(8,4),
    leg VARCHAR(20),
    opening_strategy VARCHAR(20),
    closing_strategy VARCHAR(20),
    UNIQUE(id)
);

INSERT INTO ops (op) VALUES ('migration V0001__initial_schema_chesterton.sql');
