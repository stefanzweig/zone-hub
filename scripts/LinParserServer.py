from IDL.thrift.CommonNode.ttypes import *
from IDL.thrift.LinParserNode.ttypes import *
from IDL.thrift.LinParserNode import linParserNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from zone import BaseNodeData


class LinParserNode:
    def addDbfile(self, req: filePath):
        return result(result=0, reason="")

    def setChannelConfig(self, req: linChannelConfigs):
        return result(result=0, reason="")

    def setNodeSimulation(self, req: linNodeConfig):
        return result(result=0, reason="")

    def setFrameSimulation(self, req: linFrameConfig):
        return result(result=0, reason="")

    def setFrameData(self, req: linFrameData):
        return result(result=0, reason="")

    def SetSignalData(self, req: linSignalData):
        return result(result=0, reason="")

    def clearSubscribe(self):
        return result(result=0, reason="")

    def clearDbfile(self):
        return result(result=0, reason="")

    def getStatus(self):
        return linParserStatus()

    def getLdfJsonTree(self):
        return linLdfJson

    def convertLinDbToPy(self, req: convertInput):
        return result(result=0, reason="")

    def convertLinDbToJson(self, req: convertInput):
        return result(result=0, reason="")

    def setCrcConfig(self, req: linCrcConfigParser):
        return result(result=0, reason="")

    def clearCrcConfig(self, req: linCrcConfigParser):
        return result(result=0, reason="")


if __name__ == "__main__":
    handler = LinParserNode()
    processor = linParserNode.Processor(handler)

    transport = TSocket.TServerSocket(
        host=BaseNodeData.LIN_PARSER_NODE_IP,
        port=BaseNodeData.LIN_PARSER_NODE_PORT,
    )
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting the LinParserNode server...")
    server.serve()
