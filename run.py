# --*-- coding:utf8 --*--
import sys, os, json
from aiohttp import web
from jsonrpcserver.aio import methods


async def handle(request):
    request = await request.text()

    request = json.loads(request)

    method_url_split = request['method'].split(".")
    if len(method_url_split) == 2:
        api_class = method_url_split[0]
        api_method = method_url_split[1]
        class_module = __import__("api.%s" % api_class, globals=globals(), locals=locals(), fromlist=[''])
        getattr(class_module, api_method)
        request['method'] = api_method

    response = await methods.dispatch(json.dumps(request))

    if response.is_notification:
        return web.Response()
    else:
        return web.json_response(response, status=response.http_status)


app = web.Application()
app.router.add_post('/', handle)


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    web.run_app(app, port=5000)