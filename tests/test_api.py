from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from app import app_factory
from src.database.db_utils import add_asset
from config import PROJECT_NAME, API_V1_ADDRESS

from tests.fixtures import test_assets_data


class TestApi(AioHTTPTestCase):
    async def get_application(self):
        return app_factory()

    # Fill database with original API data
    async def fill_test_data(self):
        for asset_data in test_assets_data:
            async with self.app['db'].acquire() as conn:
                await add_asset(conn, **asset_data)

    @unittest_run_loop
    async def test_index(self):
        resp = await self.client.request("GET", "/")
        self.assertEqual(resp.status, 200)
        text = await resp.text()
        self.assertIn(PROJECT_NAME, text)

    @unittest_run_loop
    async def test_assets(self):
        await self.fill_test_data()
        resp = await self.client.request("GET", f"{API_V1_ADDRESS}/assets")
        self.assertEqual(resp.status, 200)
        json_data = await resp.json()
        self.assertIsInstance(json_data, dict)

