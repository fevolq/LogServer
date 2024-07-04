#!-*- coding:utf-8 -*-
# FileName:

from dao import mongoDB


def submit(project: str, doc: dict):
    res = mongoDB.execute(project, 'insert_one', doc)
    return {
        'code': 200 if res['success'] else 400,
        'msg': res['result'].acknowledged if res['success'] else res['result'],
    }
