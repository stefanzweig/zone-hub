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

from IDL.thrift.CanParserNode import canParserNode
import BaseNodeData


class CanParserClient(object):
    """class CanParserClient docstring"""

    def __init__(self) -> None:
        """constructor docstring"""
        transport = TSocket.TSocket(
            BaseNodeData.CAN_PARSER_NODE_IP, BaseNodeData.CAN_PARSER_NODE_PORT
        )
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = canParserNode.Client(protocol)
        transport.open()

    def checkAlive(self):
        """
        检查存活度

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.checkAlive()

    def setCrcRcConfig(self, req):
        """
        设置CRC配置

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.setCrcRcConfig(req)

    def clearAllCrcRcConfig(self):
        """
        清除所有CRC配置

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.clearAllCrcRcConfig()

    def clearCrcRcConfig(self, req):
        """
        清除CRC配置

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.clearCrcRcConfig(req)

    def sendCanFrameCyc(self, req):
        """
        发送CAN帧循环

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.sendCanFrameCyc(req)

    def sendCanPduCyc(self, req):
        """
        发送CAN PDU循环

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.send_sendCanPduCyc(req)

    def sendCanPduCycList(self, req):
        """
        发送CAN PDU 循环列表

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.sendCanPduCycList(req)

    def sendCanPdu(self, req):
        """
        发送CAN PDU

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.sendCanPdu(req)

    def addDbFile(self, req):
        """
        添加数据库文件

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.addDbFile(req)

    def setConfig(self, req):
        """
        设置配置

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.setConfig(req)

    def getCanDbConfigs(self):
        """
        获取CAN数据库配置

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.getCanDbConfigs()

    def getCanDbPath(self):
        """
        获取CAN数据库路径

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.getCanDbPath()

    def subscribeMsg(self, req):
        """
        订阅消息

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.subscribeMsg(req)

    def unSubscribeMsg(self, req):
        """
        取消消息订阅

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.unSubscribeMsg(req)

    def getCanDbInfo(self):
        """
        获取CAN数据库信息

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.getCanDbInfo()

    def clear(self):
        """
        清理

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.clear()

    def clearSubscribe(self):
        """
        清理订阅

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.clearSubscribe()

    def encodePdu(self, req):
        """
        编码PDU

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.encodePdu()

    def convertCanDbToPy(self, req):
        """
        将CAN数据库转换成python文件

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.convertCanDbToPy()

    def convertCanDbToJson(self, req):
        """
        将CAN数据库转换成JSON

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.convertCanDbToJson(req)

    def updateCanPdu(self, req):
        """
        更新CAN PDU

        :return: 返回值说明.

        :rtype: result
        """
        return self.client.updateCanPdu(req)


if __name__ == "__main__":
    canParser_Client = CanParserClient()
    print(f"Client {canParser_Client} is made.")
