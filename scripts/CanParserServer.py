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
        print("checkAlive")
        return result(result=0, reason="Aliveness checked.")

    def setCrcRcConfig(self, req: pduCrcRcConfig):
        print("setCrcRcConfig")
        return result(result=0, reason="setCrcRcConfig")

    def clearAllCrcRcConfig(self):
        print("clearAllCrcRcConfig")
        return result(result=0, reason="clearAllCrcRcConfig")

    def clearCrcRcConfig(self, req: pduCrcRcConfig):
        print("clearCrcRcConfig")
        return result(result=0, reason="clearCrcRcConfig")

    def sendCanFrameCyc(self, req: canMessage):
        print("sendCanFrameCyc")
        return result(result=0, reason="sendCanFrameCyc")

    def sendCanPduCyc(self, req: pduMessage):
        print("sendCanPduCyc")
        return result(result=0, reason="sendCanPduCyc")

    def sendCanPduCycList(self, req: pduMessages):
        print("sendCanPduCycList")
        return result(result=0, reason="sendCanPduCycList")

    def sendCanPdu(self, req: pduMessage):
        print("sendCanPdu")
        return result(result=0, reason="sendCanPdu")

    def addDbFile(self, req: dbPath):
        print("addDbFile")
        return result(result=0, reason="addDbFile")

    def setConfig(self, req: dbConfigs):
        print("setConfig")
        return result(result=0, reason="setConfig")

    def getCanDbConfigs(self):
        print("getCanDbConfigs")
        return dbConfigs()

    def subscribeMsg(self, req: subscribeInfo):
        print("subscribeMsg")
        return result(result=0, reason="subscribeMsg")

    def unSubscribeMsg(self, req: subscribeInfo):
        print("unSubscribeMsg")
        return result(result=0, reason="unSubscribeMsg")

    def getCanDbInfo(self):
        print("getCanDbInfo")
        return canDbInfo()

    def clear(self):
        print("clear")
        return result(result=0, reason="cleared")

    def clearSubscribe(self):
        print("clearSubscribe")
        return result(result=0, reason="clearSubscribe")

    def encodePdu(self, req: iSignalIPduObj):
        print("encodePdu")
        return iSignalIPduEncode()

    def convertCanDbToPy(self, req: convertInput):
        print("convertCanDbToPy")
        return result(result=0, reason="convertCanDbToPy")

    def convertCanDbToJson(self, req: convertInput):
        print("convertCanDbToJson")
        return result(result=0, reason="convertCanDbToJson")

    def updateCanPdu(req: pduUpdate):
        print("updateCanPdu")
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
