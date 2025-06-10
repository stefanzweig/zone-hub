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

        Returns:

        """
        pass

    def setCrcRcConfig(self, req):
        """

        Returns:

        """
        pass

    def clearAllCrcRcConfig(self):
        """

        Returns:

        """
        pass

    def clearCrcRcConfig(self, req):
        """

        Returns:

        """
        pass

    def sendCanFrameCyc(self, req):
        """

        Returns:

        """
        pass

    def sendCanPduCyc(self, req):
        """

        Returns:

        """
        pass

    def sendCanPduCycList(self, req):
        """

        Returns:

        """
        pass

    def sendCanPdu(self, req):
        """

        Returns:

        """
        pass

    def addDbFile(self, req):
        """

        Returns:

        """
        pass

    def setConfig(self, req):
        """

        Returns:

        """
        pass

    def getCanDbConfigs(self):
        """

        Returns:

        """
        pass

    def getCanDbPath(self):
        """

        Returns:

        """
        pass

    def subscribeMsg(self, req):
        """

        Returns:

        """
        pass

    def unSubscribeMsg(self, req):
        """

        Returns:

        """
        pass

    def getCanDbInfo(self):
        """

        Returns:

        """
        pass

    def clear(self):
        """

        Returns:

        """
        pass

    def clearSubscribe(self):
        """

        Returns:

        """
        pass

    def encodePdu(self, req):
        """

        Returns:

        """
        pass

    def convertCanDbToPy(self, req):
        """

        Returns:

        """
        pass

    def convertCanDbToJson(self, req):
        """

        Returns:

        """
        pass

    def updateCanPdu(self, req):
        """

        Returns:

        """
        pass


if __name__ == "__main__":
    canParser_Client = CanParserClient()
    print(f"Client {canParser_Client} is made.")
