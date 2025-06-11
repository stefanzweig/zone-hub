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
from IDL.thrift.ConfigNode.constants import *
from IDL.thrift.SomeIpNode.ttypes import *
from IDL.thrift.CommonNode.ttypes import *

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
    """class ConfigClient docstring"""

    def __init__(self) -> None:
        """constructor ConfigClient docstring"""
        transport = TSocket.TSocket(
            BaseNodeData.CONFIG_NODE_IP, BaseNodeData.CONFIG_NODE_PORT
        )
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = configNode.Client(protocol)
        transport.open()

    def getHardwareInfo(self, type_: hardwareType) -> hardwareInfos:
        """
        获取硬件信息

        :return: 硬件信息列表

        :rtype: hardwareInfos，列表
        """
        return self.client.getHardwareInfo(type_)

    def sendCanArxml(self, dbpath: dbPath) -> canCluster:
        """
        发送CAN Arxml

        :param dbpath: 数据库文件路径

        :return: 解析完arxml后返回所有通道名字信息

        :rtype: canCluster，列表
        """
        return self.client.sendCanArxml(dbpath)

    def sendCanConfig(self, config: canConfigInfo) -> result:
        """
        发送CAN配置

        :param config: 多条CAN通道列表

        :return: 执行结果

        :rtype: result
        """
        return self.client.sendCanConfig(config)

    def sendLinConfig(self, configs: linChannelConfigs) -> result:
        """
        发送LIN配置

        :param configs: 多条LIN配置信息

        :return: 执行结果

        :rtype: result
        """
        return self.client.sendLinConfig(configs)

    def sendEthConfig(self, config: someipStackConfig) -> result:
        """
        发送ETH配置

        :param config: SomeIP配置信息

        :return: 执行结果

        :rtype: result
        """
        return self.client.sendEthConfig(config)


if __name__ == "__main__":
    config_Client = ConfigClient()
    print(f"Client {config_Client} is made.")
