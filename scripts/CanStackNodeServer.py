from IDL.thrift.CommonNode.ttypes import *
from IDL.thrift.CanStackNode.ttypes import *
from IDL.thrift.CanStackNode import canStackNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class CanStackNode:

    def checkAlive(self):
        return result(result=0, reason="")

    def getVersion(self):
        return version()

    def setConfigs(self, req:canChannelConfigs):
        return result(result=0, reason="")

    def startCanStack(self):
        return result(result=0, reason="")

    def stopCanStack(self):
        return result(result=0, reason="")

    def clearSend(self):
        return result(result=0, reason="")

    def setCrcRcConfig(self, req: frameCrcRcConfig):
        return result(result=0, reason="")

    def clearCrcRcConfig(self, req:frameCrcRcConfig):
        return result(result=0, reason="")

    def clearAllCrcRcConfig(self):
        return result(result=0, reason="")

    def sendCanMessageCycList(self, req:canMessages):
        return result(result=0, reason="")

    def sendCanMessageCyc(self, req:canMessage):
        return result(result=0, reason="")

    def sendCanMessage(self, req:canMessage):
        return result(result=0, reason="")

    def sendCanMessages(self, req:canMessages, stmin:int):
        return result(result=0, reason="")

    def getStackStatus(self):
        return result(result=0, reason="")

    def stopChannelSendCyc(self, req:channel):
        return result(result=0, reason="")

    def sendCan(self, req:canMessage):
        return result(result=0, reason="")

    def getChannelBusloadCurrent(self, req:channel):
        return busload()

    def getChannelBusloadMax(self, req:channel):
        return busload()

    def getChannelBusloadAvg(self, req:channel):
        return busload()

    def getChannelErrorFrameTotal(self, req:channel):
        return errorFrameTotal()


if __name__ == "__main__":
    handler = CanStackNode()
    processor = canStackNode.Processor(handler)

    transport = TSocket.TServerSocket(host='127.0.0.1', port=9091)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting the CanStackNode server...")
    server.serve()