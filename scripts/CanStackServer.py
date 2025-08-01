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
        print("checkAlive")
        return result(result=0, reason="checkAlive...")

    def getVersion(self):
        print("getVersion")
        return version()

    def setConfigs(self, req: canChannelConfigs):
        print("setConfigs")
        return result(result=0, reason="setConfigs...")

    def startCanStack(self):
        print("startCanStack")
        return result(result=0, reason="startCanStack...")

    def stopCanStack(self):
        print("stopCanStack")
        return result(result=0, reason="stopCanStack...")

    def clearSend(self):
        print("clearSend")
        return result(result=0, reason="clearSend...")

    def setCrcRcConfig(self, req: frameCrcRcConfig):
        print("setCrcRcConfig")
        return result(result=0, reason="setCrcRcConfig...")

    def clearCrcRcConfig(self, req: frameCrcRcConfig):
        print("clearCrcRcConfig")
        return result(result=0, reason="clearCrcRcConfig")

    def clearAllCrcRcConfig(self):
        print("clearAllCrcRcConfig")
        return result(result=0, reason="clearAllCrcRcConfig")

    def sendCanMessageCycList(self, req: canMessages):
        print("sendCanMessageCycList")
        return result(result=0, reason="sendCanMessageCycList")

    def sendCanMessageCyc(self, req: canMessage):
        print("sendCanMessageCyc")
        return result(result=0, reason="sendCanMessageCyc")

    def sendCanMessage(self, req: canMessage):
        print("sendCanMessage")
        return result(result=0, reason="sendCanMessage")

    def sendCanMessages(self, req: canMessages, stmin: int):
        print("sendCanMessages")
        return result(result=0, reason="sendCanMessages")

    def getStackStatus(self):
        print("getStackStatus")
        return result(result=0, reason="getStackStatus")

    def stopChannelSendCyc(self, req: channel):
        print("stopChannelSendCyc")
        return result(result=0, reason="stopChannelSendCyc")

    def sendCan(self, req: canMessage):
        print("sendCan")
        return result(result=0, reason="sendCan")

    def getChannelBusloadCurrent(self, req: channel):
        print("getChannelBusloadCurrent")
        return busload()

    def getChannelBusloadMax(self, req: channel):
        print("getChannelBusloadMax")
        return busload()

    def getChannelBusloadAvg(self, req: channel):
        print("getChannelBusloadAvg")
        return busload()

    def getChannelErrorFrameTotal(self, req: channel):
        print("getChannelErrorFrameTotal")
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
