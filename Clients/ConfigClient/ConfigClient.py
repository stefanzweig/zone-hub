import sys, os, logging
import time, json, traceback
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from typing import Union
import functools


from pathlib import Path

import BaseNodeData

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

from IDL.thrift.ConfigNode import configNode


class ConfigClient(object):
    """class ConfigClient docstring """
    def __init__(self) -> None:
        """constructor ConfigClient docstring """
        transport = TSocket.TSocket(
            BaseNodeData.CONFIG_NODE_IP, BaseNodeData.CONFIG_NODE_PORT
        )
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = configNode.Client(protocol)
        transport.open()


if __name__ == "__main__":
    config_Client = ConfigClient()
    print(f"Client {config_Client} is made.")
