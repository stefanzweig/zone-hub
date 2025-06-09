import sys, os, logging
import time, json, traceback
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from typing import Union
import functools


from pathlib import Path

try:
    project_root = Path(__file__).resolve().parent.parent.parent
    thrift_dir = project_root / "IDL" / "thrift"
    if not thrift_dir.exists():
        raise FileNotFoundError(f"Thrift目录不存在: {thrift_dir}")

    for path in [project_root, thrift_dir]:
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.append(path_str)
except Exception as e:
    print(f"路径添加失败: {e}")
    raise

from IDL.thrift.CanStackNode import canStackNode
from IDL.thrift.CanStackNode.ttypes import *
from IDL.thrift.CanStackNode.constants import *
from IDL.thrift.CommonNode.ttypes import *
import BaseNodeData


class CANStackClient(object):
    """定义一个CAN Stack的客户端实例"""

    def __init__(self) -> None:
        """初始化CAN Stack的客户端"""
        transport = TSocket.TSocket(
            BaseNodeData.CAN_STACK_NODE_IP, BaseNodeData.CAN_STACK_NODE_PORT
        )
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = canStackNode.Client(protocol)
        transport.open()

    def show_all_methods(self) -> None:
        """显示所有的方法"""
        return None

    def show_all_methods_with_args(self, **args) -> None:
        """
        带参数显示所有的方法

        :param args: 参数， 字典类型
        """
        return None


if __name__ == "__main__":
    canStack_Client = CANStackClient()
    print(f"Client {canStack_Client} is made.")
