#!-*- coding:utf-8 -*-
# FileName:

from enum import Enum

from fastapi import APIRouter, Query, Request
from pydantic import BaseModel

from module.log_s import logic
from utils import log_sls

prefix = 'log'
router = APIRouter(
    prefix=f'/{prefix}',
    tags=[prefix],
)


class LogDoc(BaseModel):
    project: str = Query(..., description='所属项目')
    doc: dict = Query(..., description='日志文档')


@router.post('/submit')
async def submit(req: LogDoc):
    log_sls.info(prefix, 'submit 接收参数', project=req.project)
    assert req.project, '无效 project'
    assert req.doc, '无效 doc'

    return logic.submit(req.project, req.doc)


class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class TimeMode(str, Enum):
    M5 = 'M5'
    M10 = 'M10'
    M30 = 'M30'
    H1 = 'H1'
    H2 = 'H2'
    H3 = 'H3'
    H6 = 'H6'
    H12 = 'H12'
    D1 = 'D1'
    D2 = 'D2'
    D3 = 'D3'
    D5 = 'D5'
    D7 = 'D7'


@router.get('/search/{project}')
async def search(
        project: str,

        req: Request,

        sort: bool = Query(default=True, description='排序（True倒序、False顺序）'),
        limit: int = Query(default=-1, description='条数', ge=-1),
        time_mode: TimeMode = Query(default=TimeMode.M5, description='时间等级', ),
        level: LogLevel = Query(default='', description='日志等级'),
        module_str: str = Query(default='', description='', alias='module'),
):
    assert project, '无效 project'
    extra_param = dict(req.query_params)
    log_sls.info(prefix, 'search 接收参数', project=project, req=extra_param)

    for item in ['sort', 'limit', 'level', 'time_mode', 'module']:
        if item in extra_param:
            extra_param.pop(item)

    return logic.search(project,
                        sort=sort, limit=limit, time_mode=time_mode.value,
                        level=level.value if level else '', module_str=module_str,
                        extra_param=extra_param,
                        )
