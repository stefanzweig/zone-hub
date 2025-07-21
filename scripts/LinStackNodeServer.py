from IDL.thrift.CommonNode.ttypes import *
from IDL.thrift.LinStackNode.ttypes import *
from IDL.thrift.LinParserNode import linParserNode
from IDL.thrift.LinStackNode import linStackNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from zone import BaseNodeData


class LinStackNode:
    def reset(self):
        return result(result=0, reason="reset")

    def setConfig(self, req: genericString):
        return result(result=0, reason="setConfig")

    def setChannelConig(self, req: linChannelConfigs):
        return result(result=0, reason="setChannelConig")

    def startLinStack(self):
        return result(result=0, reason="startLinStack")

    def stopLinStack(self):
        return result(result=0, reason="stopLinStack")

    def setMessageSimulation(self, req: linMessageConfig):
        return result(result=0, reason="setMessageSimulation")

    def setHeaderSimulation(self, req: linHeaderConfig):
        return result(result=0, reason="setHeaderSimulation")

    def setMessageData(self, req: linMessageDataT):
        return result(result=0, reason="setMessageData")

    def getStatus(self):
        return linStackStatus()

    def clearSubscribe(self):
        return result(result=0, reason="clearSubscribe")

    def clearSend(self, req: genericInt):
        return result(result=0, reason="clearSend")

    def setLinCrcConfig(self, req: linCrcConfig):
        return result(result=0, reason="setLinCrcConfig")

    def clearLinCrcConfig(self, req: linCrcConfig):
        return result(result=0, reason="clearLinCrcConfig")

    def getDeltaTime(self):
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
    print("Starting the LinStackNode server...")
    server.serve()
