# WARNING
Project under development and should be considered alpha.

I am not responsible for loss or gains incurred while using this code.

Use at your own risk!!

</hr>

# chesterton
A delightful little trading bot for Robinhood.

## features
- [ ] download options trading data to local PostgreSQL db
- [ ] see current delta/theta/gamma/vega numbers per contract and stock.
- [ ] group option contracts together

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



## todos
list,
- [ ] have templates load the UI js app
- [ ] fetch data from RH inline, don't use workers
