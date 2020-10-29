""" ASGI-Tools -- Tools to make ASGI Applications """

__version__ = "0.0.0"
__license__ = "MIT"


class ASGIError(Exception):
    pass


class ASGIDecodeError(ASGIError):
    pass


SUPPORTED_SCOPES = {'http', 'websocket'}
DEFAULT_CHARSET = 'utf-8'


from .request import Request  # noqa
from .response import Response, HTMLResponse, JSONResponse, PlainTextResponse  # noqa
from .middleware import (  # noqa
    RequestMiddleware, ResponseMiddleware, AppMiddleware, LifespanMiddleware, RouterMiddleware,
    combine, parse_response
)
