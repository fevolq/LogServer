#!-*- coding:utf-8 -*-
# FileName:

import base


def search():
    project = 'LogServer'
    end_point = f'/log/search/{project}'
    params = {
        'sort': True,
        'time_mode': 'D7',
        # 'limit': 10,
        # 'level': 'warning',
        # 'module': 'log',

        # 'doc.__content__': '测试'
    }
    res = base.request('GET', end_point, params=params)
    return res.json()


if __name__ == '__main__':
    # search()

    ...
