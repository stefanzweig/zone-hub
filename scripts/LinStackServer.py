from zone.IDL.thrift.CommonNode.ttypes import *
from zone.IDL.thrift.LinStackNode.ttypes import *
from zone.IDL.thrift.LinStackNode import linStackNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from zone import BaseNodeData


class LinStackNode:
    def reset(self):
        print("reset")
        return result(result=0, reason="reset")

    def setConfig(self, req: genericString):
        print("setConfig")
        return result(result=0, reason="setConfig")

    def setChannelConig(self, req: linChannelConfigs):
        print("setChannelConig")
        return result(result=0, reason="setChannelConig")

    def startLinStack(self):
        print("startLinStack")
        return result(result=0, reason="startLinStack")

    def stopLinStack(self):
        print("stopLinStack")
        return result(result=0, reason="stopLinStack")

    def setMessageSimulation(self, req: linMessageConfig):
        print("setMessageSimulation")
        return result(result=0, reason="setMessageSimulation")

    def setHeaderSimulation(self, req: linHeaderConfig):
        print("setHeaderSimulation")
        return result(result=0, reason="setHeaderSimulation")

    def setMessageData(self, req: linMessageDataT):
        print("setMessageData")
        return result(result=0, reason="setMessageData")

    def getStatus(self):
        print("getStatus")
        return linStackStatus()

    def clearSubscribe(self):
        print("clearSubscribe")
        return result(result=0, reason="clearSubscribe")

    def clearSend(self, req: genericInt):
        print("clearSend")
        return result(result=0, reason="clearSend")

    def setLinCrcConfig(self, req: linCrcConfig):
        print("setLinCrcConfig")
        return result(result=0, reason="setLinCrcConfig")

    def clearLinCrcConfig(self, req: linCrcConfig):
        print("clearLinCrcConfig")
        return result(result=0, reason="clearLinCrcConfig")

    def getDeltaTime(self):
        print("getDeltaTime")
        return genericInt64()


if __name__ == "__main__":
    handler = LinStackNode()
    processor = linStackNode.Processor(handler)

    transport = TSocket.TServerSocket(
        host=BaseNodeData.LIN_STACK_NODE_IP,
        port=BaseNodeData.LIN_STACK_NODE_PORT,
    )
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting the Lin Stack server...")
    server.serve()
