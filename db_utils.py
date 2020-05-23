import logging

from aiopg.sa import SAConnection as SAConn

from tables import asset


logger = logging.getLogger(__name__)


async def get_all_assets(conn: SAConn):
    cursor = await conn.execute(
        asset.select()
    )
    result = await cursor.fetchall()
    return result


async def add_asset(conn: SAConn, **asset_data):
    try:
        await conn.execute(
            asset.insert().values(**asset_data)
        )
    # TODO catch some exs
    except:
        pass


async def delete_asset(conn: SAConn, id: int):
    await conn.execute(
        asset.delete().where(asset.columns.ticker == id)
    )
