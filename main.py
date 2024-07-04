#!-*- coding:utf-8 -*-
# FileName:
import logging

import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from utils import log_init
import config
import controller

app = FastAPI()
log_init.init_logging('', datefmt='%Y-%m-%d %H:%M:%S', stream_level='INFO')


@app.get('/')
async def root():
    return RedirectResponse(url='/docs')


@app.get("/health")
async def health():
    return "Hello World"


for router in controller.routers:
    logging.info(f'注册路由：{router.prefix}')
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=config.PORT,
        # log_level='info',
    )
