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
        print("addDbfile")
        return result(result=0, reason="addDbfile")

    def setChannelConfig(self, req: linChannelConfigs):
        print("setChannelConfig")
        return result(result=0, reason="setChannelConfig")

    def setNodeSimulation(self, req: linNodeConfig):
        print("setNodeSimulation")
        return result(result=0, reason="setNodeSimulation")

    def setFrameSimulation(self, req: linFrameConfig):
        print("setFrameSimulation")
        return result(result=0, reason="setFrameSimulation")

    def setFrameData(self, req: linFrameData):
        print("setFrameData")
        return result(result=0, reason="setFrameData")

    def SetSignalData(self, req: linSignalData):
        print("SetSignalData")
        return result(result=0, reason="SetSignalData")

    def clearSubscribe(self):
        print("clearSubscribe")
        return result(result=0, reason="clearSubscribe")

    def clearDbfile(self):
        print("clearDbfile")
        return result(result=0, reason="clearDbfile")

    def getStatus(self):
        print("getStatus")
        return linParserStatus()

    def getLdfJsonTree(self):
        print("getLdfJsonTree")
        return linLdfJson

    def convertLinDbToPy(self, req: convertInput):
        print("convertLinDbToPy")
        return result(result=0, reason="convertLinDbToPy")

    def convertLinDbToJson(self, req: convertInput):
        print("convertLinDbToJson")
        return result(result=0, reason="convertLinDbToJson")

    def setCrcConfig(self, req: linCrcConfigParser):
        print("setCrcConfig")
        return result(result=0, reason="setCrcConfig")

    def clearCrcConfig(self, req: linCrcConfigParser):
        print("clearCrcConfig")
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
    print("Starting the Lin Parser server...")
    server.serve()
