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

@bp.post('/stacks')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    n = int(args.get('n'))
    return sanic.json(requests.get("http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks").json())


@bp.post('/export')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    # logger.debug("export")
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id')}/export"
    # logger.debug(url)
    content = requests.get(url).content.decode()
    # logger.debug(content)
    return sanic.json(content)


@bp.post('/list-images')
@extract_value_args()
async def f(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/registries/{args.get('registry_name')}/images?search={args.get('image_name')}"

    return sanic.json(requests.get(url).json())

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