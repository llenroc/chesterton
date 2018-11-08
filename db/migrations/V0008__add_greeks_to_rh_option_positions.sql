ALTER TABLE rh_option_positions ADD COLUMN delta NUMERIC(8,4) NULL ;
ALTER TABLE rh_option_positions ADD COLUMN theta NUMERIC(8,4) NULL ;
ALTER TABLE rh_option_positions ADD COLUMN gamma NUMERIC(8,4) NULL ;
ALTER TABLE rh_option_positions ADD COLUMN vega NUMERIC(8,4) NULL ;

INSERT INTO ops (op) VALUES ('migration V0008__add_greeks_to_rh_option_positions.sql');
