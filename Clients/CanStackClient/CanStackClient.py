import sys
import time, json, traceback
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
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


class CANStackClient(canStackNode.Iface):
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
        """
        显示所有的方法

        给文档生成留用
        """
        return None

    def show_all_methods_with_args(self, **args) -> None:
        """
        带参数显示所有的方法

        :param args: 参数， 字典类型

        给文档生成留用
        """
        return None

    def checkAlive(self) -> result:
        """
        检查活跃度

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.checkAlive()

    def getVersion(self) -> version:
        """
        获取版本

        :return: 返回值说明.
        
        :rtype: version
        """
        return self.client.getVersion()

    def setConfigs(self, configs: canChannelConfigs) -> result:
        """
        配置can通道信息

        :param configs: can通道配置信息（多个）

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.setConfigs(configs)

    def startCanStack(self) -> result:
        """
        启动CAN协议栈

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.startCanStack()

    def stopCanStack(self) -> result:
        """
        停止CAN协议栈

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.stopCanStack()

    def clearSend(self) -> result:
        """
        清除所有发送任务

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.clearSend()

    def setCrcRcConfig(self, config: frameCrcRcConfig) -> result:
        """
        设置特定Crc/Rc信息

        :param config: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.setCrcRcConfig(config)

    def clearCrcRcConfig(self, config: frameCrcRcConfig):
        """
        清除特定Crc/Rc信息

        :param config: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.clearCrcRcConfig(config)

    def clearAllCrcRcConfig(self) -> result:
        """
        清除所有Crc/Rc信息

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.clearAllCrcRcConfig()

    def sendCanMessageCyc(self, req: canMessage) -> result:
        """
        发送周期CAN报文

        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.sendCanMessageCyc(req)

    def sendCanMessage(self, req: canMessage):
        """
        发送单帧CAN报文

        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.sendCanMessage(req)

    def sendCanMessages(self, req: canMessages, stmin: int):
        """
        诊断发送连续帧使用，stmin单位毫秒

        :param req: 参数， 字典类型

        :param stmin: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.sendCanMessages(req, stmin)

    def getStackStatus(self) -> result:
        """
        获取CAN协议栈状态，result中result为1时表示正在运行

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.getStackStatus()

    def stopChannelSendCyc(self, req: channel) -> result:
        """
        停止某条软件通道上所有发送任务

        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.stopChannelSendCyc(req)

    def sendCan(self, req: canMessage):
        """
        发送CAN消息

        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.sendCan(req)

    def getChannelBusloadCurrent(self, req: channel):
        """
        获取
        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.getChannelBusloadCurrent(req)

    def getChannelBusloadMax(self, req: channel):
        """

        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.getChannelBusloadMax(req)

    def getChannelBusloadAvg(self, req: channel):
        """

        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.getChannelBusloadAvg(req)

    def getChannelErrorFrameTotal(self, req: channel):
        """

        :param req: 参数， 字典类型

        :return: 返回值说明.
        
        :rtype: result
        """
        return self.client.getChannelErrorFrameTotal(req)


if __name__ == "__main__":
    canStack_Client = CANStackClient()
    print(f"Client {canStack_Client} is made.")
