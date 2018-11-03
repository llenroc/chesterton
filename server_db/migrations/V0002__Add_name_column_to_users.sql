ALTER TABLE chesterton.users ADD COLUMN name TEXT NULL ;

INSERT INTO ops (op) VALUES ('migration V0002__Add_name_to_users.sql');
