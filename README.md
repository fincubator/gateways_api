# Gateways API
REST API for BitShares blockchain gateway

## Download
```shell script
git clone https://github.com/fincubator/gateways_api
cd gateways_api/
cp config/config.yml.example config/config.yml && cp docker-compose.yml.example docker-compose.yml && cp alembic.ini.example alembic.ini
```

if you want to use your own PostgreSQL connection data, you need to change:
* `config/config.yml`
* *postgres:environment* in `docker-compose.yml`

### Build & Run via Docker
```shell script
$ sudo docker-compose up -d --build
```


Go to http://0.0.0.0:8080/api/v1/assets/ and check it out:

`curl http://0.0.0.0:8080/api/v1/assets/`

```json
{
  "BTC": {
    "name": "Bitcoin",
    "unified_cryptoasset_id": "1",
    "can_deposit": "true",
    "can_withdraw": "true",
    "min_withdraw": "0.0018",
    "max_withdraw": "1000.0",
    "maker_fee": "0.1",
    "taker_fee": "0.1"
  },
  "USDT": {
    "name": "Tether",
    "unified_cryptoasset_id": "825",
    "can_deposit": "true",
    "can_withdraw": "true",
    "min_withdraw": "5.0",
    "max_withdraw": "100000.0",
    "maker_fee": "0.1",
    "taker_fee": "0.1"
  }
}
```