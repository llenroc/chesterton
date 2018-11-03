CREATE INDEX CONCURRENTLY users_email ON users (email);

INSERT INTO ops (op) VALUES ('migration V0003__NONTRANSACTIONAL_Add_index_on_users_email.sql');
