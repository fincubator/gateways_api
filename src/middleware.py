import logging
from aiohttp.web import middleware
import asyncio

logger = logging.getLogger(__name__)


@middleware
async def request_middleware(request, handler):
    # TODO some mw
    resp = await handler(request)
    return resp


def init_middleware(app) -> None:
    app.middlewares.append(request_middleware)
