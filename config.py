#!-*- coding:utf-8 -*-
# FileName:

import os

# -------------------------------SYSTEM--------------------------------
PORT = int(os.getenv('PORT', 8000))
TZ = os.getenv('TZ', 'Asia/Shanghai')
# ---------------------------------------------------------------------

# -------------------------------DB------------------------------------
MONGO_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
MONGO_PORT = int(os.getenv('MYSQL_PORT', 27017))
MONGO_USER = os.getenv('MYSQL_USER', '')
MONGO_PWD = os.getenv('MYSQL_PWD', '')
MONGO_DB = os.getenv('MYSQL_DB', 'log_server')
# ---------------------------------------------------------------------

try:
    from local_config import *
except:
    pass
