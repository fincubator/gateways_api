import json

from aiohttp import web

from utils import AssetDataSchema, ValidationError
from db_utils import get_all_assets

from config import PROJECT_NAME


async def index(request):
    return web.Response(text=f"Welcome to {PROJECT_NAME}")


async def assets_view(request):
    async with request.app['db'].acquire() as conn:
        resp_data = await get_all_assets(conn)
        resp = {}
        schema = AssetDataSchema()
        for obj in resp_data:
            try:
                resp[obj['ticker']] = schema.dump(dict(obj))
            except ValidationError:
                pass
            except Exception as ex:
                pass

        return web.json_response(resp)
