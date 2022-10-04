import requests
import traceback
import json
import sanic
from bs4 import BeautifulSoup
from io import BytesIO
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
async def f1(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    response = requests.get('http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks').json()
    l = int(len(response))
    # logger.debug(f'ELLEEEE: {l}')
    names = []
    if l == 1:
        count = (f'There is {l} stack on your system: ')
        # logger.debug(f'COUNT: {count}')
        names.append(response[0]['name'])
    else:
        count = (f'There are {l} stacks on your system: ')
        # logger.debug(f'COUNT: {count}')
        for n in range(0, l):
            names.append(response[n]['name'])
    return sanic.json(f'{count} {names}')


@bp.post('/stacks_info')
@extract_value_args()
async def f2(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    return sanic.json(requests.get("http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks").json())


@bp.post('/stack_inspect')
@extract_value_args()
async def f3(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('name_stack')}/containers"
    return sanic.json(requests.get(url).json())

@bp.post('/export_stack')
@extract_value_args()
async def f4(value, args):
    # logger.debug(f'ARGS: {args}')
    # logger.debug(f'JSON: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id')}/export"
    content = requests.get(url).content.decode()
    stack_name = (requests.get(f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id')}").json())['name']
    logger.debug((f"Stack \'{stack_name}\' Exported Successfully"))
    return sanic.json(content)

###### import stack using file reader
# @bp.post('/import_stack')
# @extract_value_args(file=True)
# async def f5(file, args):
#     logger.debug(f'ARGS: {args}')
#     logger.debug(f'File Name: {file[0].name}')
#     # args = json.loads(args)
#     url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('name_new_stack')}/upload"
#     f = BytesIO(file[0].body)
#     f.name = file[0].name
#     content = requests.post(url, files={'file':f})
#     logger.debug(content.text)
#     return sanic.json('New stack created! You can use \'Stack Name\' components to verify.')

@bp.post('/import_stack')
@extract_value_args()
async def f5(value, args):
    # logger.debug(f'ARGS: {args}')
    # logger.debug(f'File Name: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('name_new_stack')}/upload"
    path = args.get('file_import').get('path')
    file_path = f"http://gateway:8080/routes/orchestrator/files/{path}"
    # logger.debug(f'FILE URL: {file_path}')
    contenuto_file = requests.get(file_path).content
    # logger.debug(contenuto_file.decode())
    f = BytesIO(contenuto_file)
    f.name = args.get('file_import').get('name')
    content = requests.post(url, files={'file':f})
    logger.debug(content.text)
    return sanic.json(f"New stack \'{args.get('name_new_stack')}\' created! You can use \'Stack Name\' components or \'Docker Utils Dashboard\' to verify it.")


@bp.post('/volumes')
@extract_value_args()
async def f6(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    return sanic.json(requests.get("http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/volumes").json())


@bp.post('/registries')
@extract_value_args()
async def f7(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    return sanic.json(requests.get("http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/registries").json())


@bp.post('/list-docker-images')
@extract_value_args()
async def f8(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/registries/{args.get('registry_name')}/images?search={args.get('image_name')}"
    return sanic.json(requests.get(url).json())


@bp.post('/list-python-lib')
@extract_value_args()
async def f9(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    url = f"https://{args.get('pypiserver')}/{args.get('python_lib')}"
    resp = requests.get(url).content.decode()
    soup = BeautifulSoup(resp, features="html.parser")
    list = soup.text.split()
    output = []
    l = int(len(list))
    if l == 0:
        output = (f'No libraries found. Check if the name you are searching for is correct')
    else:
        for count in range(0, l):
            output.append(list[count])
        output.sort(reverse=True)
    return sanic.json(output)


@bp.post('/stack_pause')
@extract_value_args()
async def f10(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')

    check = requests.get(f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id_pause')}").json()
    name = check['name']
    if name == "loko":
        output = (f"You can't pause \'{name}\' stack. In this stack run the fundamental containers for LokoAI!")
    else:
        url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id_pause')}/pause"
        requests.put(url).json()
        output = (f"Stack \'{name}\' paused")
    return sanic.json(output)


@bp.post('/stack_unpause')
@extract_value_args()
async def f11(value, args):
    logger.debug(f'ARGS: {args}')
    logger.debug(f'JSON: {value}')
    check = requests.get(f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id_unpause')}").json()
    name = check['name']
    url = f"http://docker-utils-ext_docker-utils:8080/ds4biz/ds4biz-docker/0.2/stacks/{args.get('stack_id_unpause')}/unpause"
    requests.put(url).json()
    output = (f"Stack \'{name}\' unpaused")
    return sanic.json(output)



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
