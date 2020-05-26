import logging

from aiopg.sa import SAConnection as SAConn
from sqlalchemy.orm.query import Query
from sqlalchemy.sql import insert
from models import Asset


logger = logging.getLogger(__name__)


async def get_all_assets(conn: SAConn):
    cursor = await conn.execute(str(Query(Asset).as_scalar()))
    result = await cursor.fetchall()
    return result


async def add_asset(conn: SAConn, **asset_data):
    try:
        ins = insert(table=Asset).values(**asset_data)
        await conn.execute(ins)
    except Exception as ex:
        logger.debug(ex)
    # TODO catch some exs
