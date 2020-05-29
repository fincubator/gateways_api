import logging

from aiohttp import web

from data_schemes import AssetDataSchema, CoinDataSchema, ValidationError
from db_utils import get_all_assets, get_all_coins
from config import PROJECT_NAME, API_V1_ADDRESS


routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.Response(text=f"Welcome to {PROJECT_NAME}")


@routes.get(f'{API_V1_ADDRESS}/assets/')
async def assets_view(request):
    async with request.app['db'].acquire() as conn:
        resp_data = await get_all_assets(conn)
        resp = {}
        schema = AssetDataSchema()
        for obj in resp_data:
            try:
                resp[obj['ticker']] = schema.dump(dict(obj))
            except ValidationError as ex:
                logging.debug(f"ValidationError: {ex.messages}")
            except Exception as ex:
                logging.debug(ex)

        return web.json_response(resp)


@routes.get(f'{API_V1_ADDRESS}/coins/')
async def coins_view(request):
    async with request.app['db'].acquire() as conn:
        resp_data = await get_all_coins(conn)
        resp = {}
        schema = CoinDataSchema()
        for index, obj in enumerate(resp_data):
            dict_obj = dict(obj)
            dict_obj["gate_fee"] = obj.withdraw_fee / 10 ** obj.precision
            try:
                resp[index] = schema.dump(dict_obj)
            except ValidationError as ex:
                logging.debug(f"ValidationError: {ex.messages}")
            except Exception as ex:
                logging.debug(ex)

        return web.json_response(resp)
