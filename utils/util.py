#!-*- coding:utf-8 -*-
# FileName:

import datetime

import pytz

import config


def local_time(to_str: bool = True, *, fmt='%Y-%m-%d %H:%M:%S', tz=config.TZ or 'Asia/Shanghai'):
    now = datetime.datetime.now(pytz.timezone(tz))
    result = now
    if to_str:
        result = datetime.datetime.strftime(now, fmt)
    return result
