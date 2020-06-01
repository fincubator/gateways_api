from aiohttp.web import middleware


@middleware
async def request_middleware(request, handler):
    # TODO some mw
    resp = await handler(request)
    return resp


def init_middleware(app) -> None:
    app.middlewares.append(request_middleware)
