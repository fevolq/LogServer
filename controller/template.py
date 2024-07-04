#!-*- coding:utf-8 -*-
# FileName:

from fastapi import APIRouter

from module.template import logic

prefix = 'template'
router = APIRouter(
    prefix=f'/{prefix}',
    tags=[prefix],
)


@router.get('/demo')
async def demo():
    return logic.demo()
