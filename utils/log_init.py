#!-*coding:utf-8 -*-
# FileName:

import logging
import logging.handlers
import os


def init_logging(filename,
                 file_level=logging.DEBUG,
                 error_level=logging.ERROR,
                 stream_level=logging.DEBUG,
                 daily=True,
                 datefmt='%H:%M:%S'):
    """日志初始化"""
    logging.basicConfig(level=stream_level,
                        format='%(asctime)s.%(msecs)03d %(levelname)s : %(message)s',
                        datefmt=datefmt)
    # 日志文件设置
    if filename:
        if os.path.split(filename)[0]:
            path = os.path.split(filename)[0]
            if not os.path.exists(path):
                os.makedirs(path)
        if daily:
            file_handler = logging.handlers.TimedRotatingFileHandler(filename, when='MIDNIGHT')
        else:
            file_handler = logging.FileHandler(filename)
        file_handler.setLevel(file_level)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s : %(message)s', datefmt=datefmt)
        )
        logging.getLogger().addHandler(file_handler)

        if error_level:
            if daily:
                error_file_handler = logging.handlers.TimedRotatingFileHandler(filename + ".ERROR", when='MIDNIGHT')
            else:
                error_file_handler = logging.FileHandler(filename + ".ERROR")
            error_file_handler.setLevel(error_level)
            error_file_handler.setFormatter(
                logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s : %(message)s', datefmt=datefmt)
            )
            logging.getLogger().addHandler(error_file_handler)

    class ColorCodes:
        RESET = '\033[0m'
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'

    logging.addLevelName(logging.DEBUG,
                         f"|{ColorCodes.WHITE}{logging.getLevelName(logging.DEBUG).center(7, ' ')}{ColorCodes.RESET}|")
    logging.addLevelName(logging.INFO,
                         f"|{ColorCodes.GREEN}{logging.getLevelName(logging.INFO).center(7, ' ')}{ColorCodes.RESET}|")
    logging.addLevelName(logging.WARNING,
                         f"|{ColorCodes.YELLOW}{logging.getLevelName(logging.WARNING).center(7, ' ')}{ColorCodes.RESET}|")
    logging.addLevelName(logging.ERROR,
                         f"|{ColorCodes.RED}{logging.getLevelName(logging.ERROR).center(7, ' ')}{ColorCodes.RESET}|")


if __name__ == '__main__':
    init_logging('', datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('info')
    logging.debug('debug')
    logging.warning('warning')
    logging.error('error')
