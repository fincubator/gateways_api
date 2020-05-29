import logging

from aiohttp import web
import aiopg.sa

from views import routes
from middleware import init_middleware

from config import pg_config


async def init_database(app: web.Application) -> None:
    # Async engine to execute clients requests
    engine = await aiopg.sa.create_engine(**pg_config)
    app['db'] = engine


async def close_database(app: web.Application) -> None:
    app['db'].close()
    await app['db'].wait_closed()


def app_factory() -> web.Application:
    logging.basicConfig(level=logging.DEBUG)

    app = web.Application()

    app.add_routes(routes)
    init_middleware(app)

    app.on_startup.extend([init_database])
    app.on_cleanup.extend([close_database])

    return app


gw_app = app_factory()
