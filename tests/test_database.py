from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from app import app_factory
from src.database.db_utils import get_all_assets, add_asset

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
    async def test_get_all_assets(self):
        await self.fill_test_data()
        async with self.app['db'].acquire() as conn:
            resp_data = await get_all_assets(conn)
            self.assertIsInstance(resp_data, list)
