from zone.IDL.thrift.CommonNode.ttypes import *
from zone.IDL.thrift.CanStackNode.ttypes import *
from zone.IDL.thrift.CanStackNode import canStackNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from zone import BaseNodeData


class CanStackNode:

    def checkAlive(self):
        return result(result=0, reason="checkAlive...")

    def getVersion(self):
        return version()

    def setConfigs(self, req: canChannelConfigs):
        return result(result=0, reason="setConfigs...")

    def startCanStack(self):
        return result(result=0, reason="startCanStack...")

    def stopCanStack(self):
        return result(result=0, reason="stopCanStack...")

    def clearSend(self):
        return result(result=0, reason="clearSend...")

    def setCrcRcConfig(self, req: frameCrcRcConfig):
        return result(result=0, reason="setCrcRcConfig...")

    def clearCrcRcConfig(self, req: frameCrcRcConfig):
        return result(result=0, reason="clearCrcRcConfig")

    def clearAllCrcRcConfig(self):
        return result(result=0, reason="clearAllCrcRcConfig")

    def sendCanMessageCycList(self, req: canMessages):
        return result(result=0, reason="sendCanMessageCycList")

    def sendCanMessageCyc(self, req: canMessage):
        return result(result=0, reason="sendCanMessageCyc")

    def sendCanMessage(self, req: canMessage):
        return result(result=0, reason="sendCanMessage")

    def sendCanMessages(self, req: canMessages, stmin: int):
        return result(result=0, reason="sendCanMessages")

    def getStackStatus(self):
        return result(result=0, reason="getStackStatus")

    def stopChannelSendCyc(self, req: channel):
        return result(result=0, reason="stopChannelSendCyc")

    def sendCan(self, req: canMessage):
        return result(result=0, reason="sendCan")

    def getChannelBusloadCurrent(self, req: channel):
        return busload()

    def getChannelBusloadMax(self, req: channel):
        return busload()

    def getChannelBusloadAvg(self, req: channel):
        return busload()

    def getChannelErrorFrameTotal(self, req: channel):
        return errorFrameTotal()


if __name__ == "__main__":
    handler = CanStackNode()
    processor = canStackNode.Processor(handler)

    transport = TSocket.TServerSocket(
        host=BaseNodeData.CAN_STACK_NODE_IP,
        port=BaseNodeData.CAN_STACK_NODE_PORT,
    )
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting the CAN Stack server...")
    server.serve()
