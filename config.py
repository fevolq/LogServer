#!-*- coding:utf-8 -*-
# FileName:

import os

# -------------------------------SYSTEM--------------------------------
PORT = int(os.getenv('PORT', 8000))
TZ = os.getenv('TZ', 'Asia/Shanghai')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
# ---------------------------------------------------------------------

# -------------------------------DB------------------------------------
MONGO_HOST = os.getenv('MONGO_HOST', '127.0.0.1')
MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
MONGO_USER = os.getenv('MONGO_USER', '')
MONGO_PWD = os.getenv('MONGO_PWD', '')
MONGO_DB = os.getenv('MONGO_DB', 'log_server')
# ---------------------------------------------------------------------

try:
    from local_config import *
except:
    pass
