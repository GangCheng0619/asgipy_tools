async def test_response():
    from asgi_tools import Response, parse_response

    response = Response("Content", content_type='text/html')
    response.cookies['session'] = 'test-session'
    response.cookies['session']['path'] = '/'
    assert response.body == b"Content"
    assert response.status_code == 200
    assert response.get_headers() == [
        (b"content-type", b"text/html; charset=utf-8"),
        (b'set-cookie', b'session=test-session; Path=/'),
    ]
    messages = [m async for m in response]
    assert messages
    assert messages[0] == {
        'headers': [
            (b'content-type', b'text/html; charset=utf-8'),
            (b'set-cookie', b'session=test-session; Path=/'),
            (b'content-length', b'7'),
        ],
        'status': 200,
        'type': 'http.response.start'
    }
    assert messages[1] == {'body': b'Content', 'type': 'http.response.body'}

    response = await parse_response({'test': 'passed'})
    assert response.status_code == 200
    assert response.get_headers() == [(b'content-type', b'application/json')]
    _, body = [m async for m in response]
    assert body == {'body': b'{"test": "passed"}', 'type': 'http.response.body'}

    response = await parse_response((500,))
    assert response.status_code == 500


async def test_html_response():
    from asgi_tools import HTMLResponse

    response = HTMLResponse("Content")
    assert response.body == b"Content"
    assert response.status_code == 200
    assert response.get_headers() == [
        (b"content-type", b"text/html; charset=utf-8"),
    ]


async def test_text_response():
    from asgi_tools import PlainTextResponse

    response = PlainTextResponse("Content")
    assert response.body == b"Content"
    assert response.status_code == 200
    assert response.get_headers() == [
        (b"content-type", b"text/plain; charset=utf-8"),
    ]


async def test_json_response():
    from asgi_tools import JSONResponse

    response = JSONResponse([1, 2, 3])
    assert response.body == b"[1, 2, 3]"
    assert response.status_code == 200
    assert response.get_headers() == [
        (b"content-type", b"application/json"),
    ]


async def test_redirect_response():
    from asgi_tools import RedirectResponse

    response = RedirectResponse('/logout')
    assert response.body == b""
    assert response.status_code == 307
    assert response.get_headers() == [
        (b"location", b"/logout"),
    ]


async def test_stream_response():
    import asyncio as aio
    from asgi_tools import StreamResponse

    async def fill(timeout=.001):
        for idx in range(10):
            await aio.sleep(timeout)
            yield idx

    response = StreamResponse(fill())
    messages = []
    async for msg in response:
        messages.append(msg)

    assert len(messages) == 12
    assert messages[-2] == {'body': b'9', 'more_body': True, 'type': 'http.response.body'}
    assert messages[-1] == {'body': b'', 'more_body': False, 'type': 'http.response.body'}

    def app(scope, receive, send):
        response = StreamResponse(fill())
        return response(scope, receive, send)

    from httpx import AsyncClient

    async with AsyncClient(
            app=app, base_url='http://testserver') as client:
        res = await client.get('/')
        assert res.status_code == 200
        assert res.text == '0123456789'