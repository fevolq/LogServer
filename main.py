#!-*- coding:utf-8 -*-
# FileName:
import logging

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse

from utils import log_init
import config
import controller

app = FastAPI()
log_init.init_logging('', datefmt='%Y-%m-%d %H:%M:%S', stream_level=config.LOG_LEVEL)


@app.get('/')
async def root():
    return RedirectResponse(url='/docs')


@app.get("/health")
async def health():
    return "Hello World"


@app.exception_handler(Exception)
async def exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={'code': 500, 'msg': '服务器异常', 'content': str(exc)}
    )


for router in controller.routers:
    logging.info(f'注册路由：{router.prefix}')
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=config.PORT,
        log_level=config.LOG_LEVEL.lower(),
    )
