#!-*- coding:utf-8 -*-
# FileName:

import copy
import time

from dao import mongoDB


def submit(project: str, doc: dict):
    res = mongoDB.execute(project, 'insert_one', doc)
    return {
        'code': 200 if res['success'] else 400,
        'msg': res['result'].acknowledged if res['success'] else res['result'],
    }


def search(project: str, *, sort: bool, limit: int, level: str, time_mode: str, module_str: str, extra_param: dict):
    query = copy.deepcopy(extra_param)
    options = {}

    # 时间
    time_v = int(time_mode[1:])
    if time_mode[0] == 'M':  # 分钟
        time_v *= 60
    elif time_mode[0] == 'H':  # 小时
        time_v *= 60 * 60
    elif time_mode[0] == 'D':  # 天
        time_v *= 60 * 60 * 24
    query['metadata.timestamp'] = {'$gte': time.time() - time_v}

    if level:
        query['level'] = level
    if module_str:
        query['module'] = module_str

    if limit > 0:
        options['limit'] = limit
    options['sort'] = {'metadata.timestamp': -1 if sort else 1}  # -1为倒序

    res = mongoDB.execute(project, 'find', query, {'_id': 0}, **options)
    if not res['success']:
        return {
            'code': 400,
            'msg': res['msg'],
        }
    return {'code': 200, 'data': res['result']}
