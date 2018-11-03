<hr>

# WARNING
Project under development and should be considered alpha.

I am not responsible for loss or gains incurred while using this code.

Use at your own risk!!
</hr>

# chesterton
A delightful little trading bot for Robinhood.

## development
Dev environment consists of,
1. python (python 3.6, install pipenv, and run `pipenv install`)
2. javascript (`cd ui && yarn install`)
3. PostgreSQL

  create db,
  ```sql
  -- in postgres console
  create database chesterton
  ```
  run migrations,
  ```bash
  cd db && pipenv run pgmigrate -t latest migrate
  ```

## testing
@TODO

## production
@TODO
