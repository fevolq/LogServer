#!-*- coding:utf-8 -*-
# FileName: json数据格式转换

import datetime
import json
from decimal import Decimal


class ObjEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        elif isinstance(o, bytes):
            return o.decode()
        elif isinstance(o, Decimal):
            return float(o)
        elif isinstance(o, object):
            return o.__dict__
        else:
            return json.JSONEncoder.default(self, o)
