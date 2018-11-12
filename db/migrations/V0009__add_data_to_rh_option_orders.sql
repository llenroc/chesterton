ALTER TABLE rh_option_orders ADD COLUMN data JSON NULL ;

INSERT INTO ops (op) VALUES ('migration V0009__add_data_to_rh_option_orders.sql');
