CREATE INDEX CONCURRENTLY i_users_email ON chesterton.users (email);

INSERT INTO ops (op) VALUES ('migration V0003__NONTRANSACTIONAL_Add_index_on_users_email.sql');
