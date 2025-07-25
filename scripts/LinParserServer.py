from zone.IDL.thrift.CommonNode.ttypes import *
from zone.IDL.thrift.LinParserNode.ttypes import *
from zone.IDL.thrift.LinParserNode import linParserNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from zone import BaseNodeData


class LinParserNode:
    def addDbfile(self, req: filePath):
        return result(result=0, reason="addDbfile")

    def setChannelConfig(self, req: linChannelConfigs):
        return result(result=0, reason="setChannelConfig")

    def setNodeSimulation(self, req: linNodeConfig):
        return result(result=0, reason="setNodeSimulation")

    def setFrameSimulation(self, req: linFrameConfig):
        return result(result=0, reason="setFrameSimulation")

    def setFrameData(self, req: linFrameData):
        return result(result=0, reason="setFrameData")

    def SetSignalData(self, req: linSignalData):
        return result(result=0, reason="SetSignalData")

    def clearSubscribe(self):
        return result(result=0, reason="clearSubscribe")

    def clearDbfile(self):
        return result(result=0, reason="clearDbfile")

    def getStatus(self):
        return linParserStatus()

    def getLdfJsonTree(self):
        return linLdfJson

    def convertLinDbToPy(self, req: convertInput):
        return result(result=0, reason="convertLinDbToPy")

    def convertLinDbToJson(self, req: convertInput):
        return result(result=0, reason="convertLinDbToJson")

    def setCrcConfig(self, req: linCrcConfigParser):
        return result(result=0, reason="setCrcConfig")

    def clearCrcConfig(self, req: linCrcConfigParser):
        return result(result=0, reason="clearCrcConfig")


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
