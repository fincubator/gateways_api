import logging

from aiohttp import web

from data_schemes import AssetDataSchema, CoinDataSchema, ValidationError
from db_utils import get_all_assets, get_all_coins
from config import PROJECT_NAME, API_V1_ADDRESS


routes = web.RouteTableDef()


def json_view(func):
    async def wrapped(request) -> web.json_response:
        return web.json_response(await func(request))
    return wrapped


@routes.get('/')
async def index(request):
    return web.Response(text=f"Welcome to {PROJECT_NAME}")


@routes.get(f'{API_V1_ADDRESS}/assets/')
@json_view
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

        return resp


@routes.get(f'{API_V1_ADDRESS}/coins/')
@json_view
async def coins_view(request):
    async with request.app['db'].acquire() as conn:
        resp_data = await get_all_coins(conn)

        # TODO add many=True arg
        schema = CoinDataSchema()

        # TODO replace to resp = schema.dump(resp_data)
        resp = []
        for obj in resp_data:
            dict_obj = dict(obj)
            dict_obj["gate_fee"] = obj.withdraw_fee / 10 ** obj.precision
            try:
                resp.append(schema.dump(dict_obj))
            except ValidationError as ex:
                logging.debug(f"ValidationError: {ex.messages}")
            except Exception as ex:
                logging.debug(ex)

        return resp
