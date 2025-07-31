from zone.IDL.thrift.CommonNode.ttypes import *
from zone.IDL.thrift.CanParserNode.ttypes import *
from zone.IDL.thrift.CanStackNode.ttypes import *
from zone.IDL.thrift.CanParserNode import canParserNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from zone import BaseNodeData


class CanParserNode:
    def checkAlive(self):
        return result(result=0, reason="Aliveness checked.")

    def setCrcRcConfig(self, req: pduCrcRcConfig):
        return result(result=0, reason="setCrcRcConfig")

    def clearAllCrcRcConfig(self):
        return result(result=0, reason="clearAllCrcRcConfig")

    def clearCrcRcConfig(self, req: pduCrcRcConfig):
        return result(result=0, reason="clearCrcRcConfig")

    def sendCanFrameCyc(self, req: canMessage):
        return result(result=0, reason="sendCanFrameCyc")

    def sendCanPduCyc(self, req: pduMessage):
        return result(result=0, reason="sendCanPduCyc")

    def sendCanPduCycList(self, req: pduMessages):
        return result(result=0, reason="sendCanPduCycList")

    def sendCanPdu(self, req: pduMessage):
        return result(result=0, reason="sendCanPdu")

    def addDbFile(self, req: dbPath):
        return result(result=0, reason="addDbFile")

    def setConfig(self, req: dbConfigs):
        return result(result=0, reason="setConfig")

    def getCanDbConfigs(self):
        return dbConfigs()

    def subscribeMsg(self, req: subscribeInfo):
        return result(result=0, reason="subscribeMsg")

    def unSubscribeMsg(self, req: subscribeInfo):
        return result(result=0, reason="unSubscribeMsg")

    def getCanDbInfo(self):
        return canDbInfo()

    def clear(self):
        return result(result=0, reason="cleared")

    def clearSubscribe(self):
        return result(result=0, reason="clearSubscribe")

    def encodePdu(self, req: iSignalIPduObj):
        return iSignalIPduEncode()

    def convertCanDbToPy(self, req: convertInput):
        return result(result=0, reason="convertCanDbToPy")

    def convertCanDbToJson(self, req: convertInput):
        return result(result=0, reason="convertCanDbToJson")

    def updateCanPdu(req: pduUpdate):
        return result(result=0, reason="updateCanPdu")


if __name__ == "__main__":
    handler = CanParserNode()
    processor = canParserNode.Processor(handler)

    transport = TSocket.TServerSocket(
        host=BaseNodeData.CAN_PARSER_NODE_IP,
        port=BaseNodeData.CAN_PARSER_NODE_PORT,
    )
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting the CAN Parser server...")
    server.serve()
