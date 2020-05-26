import pytest
from aiohttp import web
import sys

sys.path.append("/app")

from db_utils import add_asset
from config import PROJECT_NAME, API_V1_ADDRESS
from gw_app import app_factory
from tests.fixtures import test_assets_data


@pytest.fixture
def cli(loop, aiohttp_client):
    app = app_factory()
    return loop.run_until_complete(aiohttp_client(app))


async def test_index(cli):
    resp = await cli.get('/')
    assert resp.status == 200
    assert PROJECT_NAME in await resp.text()


async def test_assets(cli):
    for asset_data in test_assets_data:
        async with cli.server.app['db'].acquire() as conn:
            await add_asset(conn, **asset_data)
    resp = await cli.get(F"{API_V1_ADDRESS}/assets/")
    assert resp.status == 200
    json_data = await resp.json()
    assert isinstance(json_data, dict)
