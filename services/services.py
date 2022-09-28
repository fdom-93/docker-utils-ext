import requests
import traceback
import sanic
from sanic import Sanic, Blueprint
from sanic.exceptions import NotFound
from sanic_openapi import swagger_blueprint
from loko_extensions.business.decorators import extract_value_args
from utils.logger_utils import stream_logger
logger = stream_logger(__name__)
def get_app(name):
    app = Sanic(name)
    swagger_blueprint.url_prefix = "/api"
    app.blueprint(swagger_blueprint)
    return app

name = "first_project"
app = get_app(name)
bp = Blueprint("default", url_prefix=f"/")
app.config["API_TITLE"] = name


@bp.post('/stacks_name')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    response = requests.get('http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks').json()
    l = int(len(response))
    names = []
    if l == 1:
        count = (f'There is {l} stack on your system: ')
        names.append(response[l]['name'])
    else:
        count = (f'There are {l} stacks on your system: ')
        for n in range(0, l):
            names.append(response[n]['name'])
    return sanic.json((f'{count} {names}'))


@bp.post('/stacks_info')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    return sanic.json(requests.get("http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks").json())


@bp.post('/stack_inspect')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('name_stack')}/containers"
    return sanic.json(requests.get(url).json())

@bp.post('/export')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id')}/export"
    content = requests.get(url).content.decode()
    return sanic.json(content)


@bp.post('/list-images')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/registries/{args.get('registry_name')}/images?search={args.get('image_name')}"
    return sanic.json(requests.get(url).json())



@bp.post('/registries')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    return sanic.json(requests.get("http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/registries").json())


@bp.post('/volumes')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    return sanic.json(requests.get("http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/volumes").json())



@app.exception(Exception)
async def manage_exception(request, exception):
    e = dict(error=str(exception))
    if isinstance(exception, NotFound):
        return sanic.json(e, status=404)
    logger.error('TracebackERROR: \n' + traceback.format_exc() + '\n\n')
    status_code = exception.status_code or 500
    return sanic.json(e, status=status_code)


app.blueprint(bp)

app.run("0.0.0.0", port=8080, auto_reload=True)