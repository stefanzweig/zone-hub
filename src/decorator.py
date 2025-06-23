import os
import sys
import time
from pathlib import Path
from functools import wraps

"""
这个模块定义一些修饰器
"""


def singleton(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):  # 改名为wrapper更明确，修正kwargs拼写
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]  # 简化了条件判断

    return wrapper
