import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from nomad.config import config

myapi_entry_point = config.get_plugin_entry_point(
    'crc1415_about.apis:crc1415_about_footer_pages'
)

app = FastAPI(root_path=f'{config.services.api_base_path}/{myapi_entry_point.prefix}')

static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
app.mount('/static', StaticFiles(directory=static_folder), name='static')
