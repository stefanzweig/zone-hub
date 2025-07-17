from IDL.thrift.CommonNode.ttypes import *
from IDL.thrift.CanParserNode.ttypes import *
from IDL.thrift.CanStackNode.ttypes import *
from IDL.thrift.CanParserNode import canParserNode
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class CanParserNode:
    def checkAlive(self):

        return result(result=0, reason="")
    
    def setCrcRcConfig(self, req:pduCrcRcConfig):

        return result(result=0, reason="")
    
    def clearAllCrcRcConfig(self):

        return result(result=0, reason="")

    def clearCrcRcConfig (self, req: pduCrcRcConfig):

        return result(result=0, reason="")
    
    def sendCanFrameCyc(self, req: canMessage):

        return result(result=0, reason="")

    def sendCanPduCyc(self, req: pduMessage):

        return result(result=0, reason="")
    
    def sendCanPduCycList(self, req: pduMessages):
        
        return result(result=0, reason="")

    def sendCanPdu(self, req: pduMessage):
         
         return result(result=0, reason="")
    
    def addDbFile(self, req: dbPath):
        
        return result(result=0, reason="")

    def setConfig(self, req: dbConfigs):
        
        return result(result=0, reason="")
    
    def getCanDbConfigs(self):

        return dbConfigs()
    
    def subscribeMsg(self, req:subscribeInfo):

        return result(result=0, reason="")
    
    def unSubscribeMsg(self, req:subscribeInfo):

        return result(result=0, reason="")
    
    def getCanDbInfo(self):

        return canDbInfo()
    
    def clear(self):
        
        return result(result=0, reason="")
    
    def clearSubscribe(self):

        return result(result=0, reason="")

    def encodePdu(self, req:iSignalIPduObj):

        return iSignalIPduEncode()
    
    def convertCanDbToPy(self, req:convertInput):

        return result(result=0, reason="")
    
    def convertCanDbToJson(self, req:convertInput):

        return result(result=0, reason="")
    
    def updateCanPdu(req:pduUpdate):

        return result(result=0, reason="")
    
if __name__ == "__main__":
    handler = CanParserNode()
    processor = canParserNode.Processor(handler)

    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting the server...")
    server.serve()
