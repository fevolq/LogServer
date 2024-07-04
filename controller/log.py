#!-*- coding:utf-8 -*-
# FileName:

from fastapi import APIRouter, Query
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
    log_sls.info('log', '接收参数', project=req.project)
    assert req.project, '无效 project'
    assert req.doc, '无效 doc'

    return logic.submit(req.project, req.doc)
