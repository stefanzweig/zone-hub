from IDL.thrift.CommonNode.ttypes import *
from IDL.thrift.LinStackNode.ttypes import *
from IDL.thrift.LinParserNode import linParserNode
from IDL.thrift.LinStackNode import linStackNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class LinStackNode:
    def reset(self):
        return result(result=0, reason="")

    def setConfig(self, req:genericString):
        return result(result=0, reason="")

    def setChannelConig(self, req:linChannelConfigs):
        return result(result=0, reason="")

    def startLinStack(self):
        return result(result=0, reason="")

    def stopLinStack(self):
        return result(result=0, reason="")

    def setMessageSimulation(self, req:linMessageConfig):
        return result(result=0, reason="")

    def setHeaderSimulation(self, req:linHeaderConfig):
        return result(result=0, reason="")

    def setMessageData(self, req:linMessageDataT):
        return result(result=0, reason="")

    def getStatus(self):
        return linStackStatus()

    def clearSubscribe(self):
        return result(result=0, reason="")

    def clearSend(self, req:genericInt):
        return result(result=0, reason="")

    def setLinCrcConfig(self, req:linCrcConfig):
        return result(result=0, reason="")

    def clearLinCrcConfig(self, req:linCrcConfig):
        return result(result=0, reason="")

    def getDeltaTime(self):
        return genericInt64()

if __name__ == "__main__":
    handler = LinStackNode()
    processor = linStackNode.Processor(handler)

    transport = TSocket.TServerSocket(host='127.0.0.1', port=9092)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting the LinStackNode server...")
    server.serve()