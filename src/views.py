import json

from aiohttp import web

# TODO remove this in prod
from src import __version__

from src.utils import alchemy_encoder
from src.database.db_utils import get_all_assets

from config import PROJECT_NAME


async def index(request):
    return web.Response(text=f"Welcome to {PROJECT_NAME} {__version__}")


async def assets_view(request):
    async with request.app['db'].acquire() as conn:
        resp_data = await get_all_assets(conn)
        resp = {}
        for obj in resp_data:
            resp[obj['ticker']] = dict(obj)
            resp[obj['ticker']].pop("id")
            resp[obj['ticker']].pop("ticker")

        dumps = json.dumps(resp, default=alchemy_encoder)

        # This needs to convert decimal types in JSON-response to strings.
        # Remove this if you want to normal types in response
        dumps = dumps.replace('true', '"true"').replace('false', '"false"')
        to_string_kwargs = dict(parse_float=str, parse_int=str)

        loads = json.loads(dumps, **to_string_kwargs)
        return web.json_response(loads)
