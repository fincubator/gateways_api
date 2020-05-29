import logging

from aiopg.sa import SAConnection as SAConn
from sqlalchemy.orm.query import Query
from sqlalchemy.sql import insert
from models import Asset, Coin


async def get_all_assets(conn: SAConn):
    cursor = await conn.execute(str(Query(Asset).as_scalar()))
    result = await cursor.fetchall()
    return result


async def get_all_coins(conn: SAConn):
    cursor = await conn.execute(str(Query(Coin).as_scalar()))
    result = await cursor.fetchall()
    return result


async def add_asset(conn: SAConn, **asset_data):
    try:
        ins = insert(table=Asset).values(**asset_data)
        await conn.execute(ins)
    except Exception as ex:
        logging.debug(ex)


async def add_coin(conn: SAConn, **coin_data):
    try:
        ins = insert(table=Coin).values(**coin_data)
        await conn.execute(ins)
    except Exception as ex:
        logging.debug(ex)
