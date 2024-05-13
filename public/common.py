# 自定义异常类
import os
import sys
import time
from loguru import logger

from config.pathconf import LOG_DIR


class ErrorExcep(Exception):
    """
    自定义异常类
    """

    def __init__(self, message):
        super().__init__(message)
# 日志设置类
class SetLog:
    """
    日志设置类  使用 logger 请从此logs目录导入
    """

    DAY = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    LOG_PATH = os.path.join(LOG_DIR, f'{DAY}_all.log')

    ERR_LOG_PATH = os.path.join(LOG_DIR, f'{DAY}_err.log')

    logger.add(LOG_PATH, rotation="00:00", encoding='utf-8')

    logger.add(ERR_LOG_PATH, rotation="00:00", encoding='utf-8', level='ERROR', )
    logger.remove()  # 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
    handler_id = logger.add(sys.stderr, level="DEBUG")  # 添加一个可以修改控制的handler

