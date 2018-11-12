ALTER TABLE rh_option_orders ALTER COLUMN leg TYPE INTEGER USING leg::integer;

INSERT INTO ops (op) VALUES ('migration V0010__change_leg_to_integer_rh_option_orders.sql');
