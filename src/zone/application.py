import os
import sys
import time
import typing
from pathlib import Path
from typing import Union, Callable
from .utils.dsx import as_list
from .utils.config import (
    CAN_Config,
    LIN_Config,
    ETH_Config_PC,
    ETH_Config_Vector,
)
from .utils.snippets import normalize_components

from zone.clients import (
    canstackclient,
    canparserclient,
    linstackclient,
    linparserclient,
)


# APIs for the test suites' development.
def create_can_client():
    pass


def create_canparser_client():
    pass


def create_configs():
    pass


class App(object):
    """ """

    def __init__(
        self,
        *,
        configs=None,
        connections=None,
        canstack=None,
        canparser=None,
        linstack=None,
        linparser=None,
        data=None
    ) -> None:
        self._configs = as_list(configs)
        self._connections = as_list(connections)
        self._clients = []
        self._canstack = canstack or canstackclient
        self._canparser = canparser or canparserclient
        self._linstack = linstack or linstackclient
        self._linparser = linparser or linparserclient
        self._data = data
        self._clients = {
            "canstack": self._canstack,
            "canparser": self._canparser,
            "linstack": self._linstack,
            "linparser": self._linparser,
        }

    @property
    def Configs(self):
        return self._configs

    @Configs.setter
    def Configs(self, value):
        self._configs = as_list(value)

    @property
    def Connections(self):
        return self._connections

    @Connections.setter
    def Connections(self, value):
        self._connections = as_list(value)

    @property
    def CanStack(self):
        return self._canstack

    @CanStack.setter
    def CanStack(self, value):
        self._canstack = value

    @property
    def CanParser(self):

        return self._canparser

    @CanParser.setter
    def CanParser(self, value):
        self._canparser = value

    @property
    def LinStack(self):
        return self._linstack

    @LinStack.setter
    def LinStack(self, value):
        self._linstack = value

    @property
    def LinParser(self):
        return self._linparser

    @LinParser.setter
    def LinParser(self, value):
        self._linparser = value

    @property
    def Clients(self):
        return self._clients

    @property
    def DataModel(self):
        return self._data

    # api
    def connect(self, components=None):
        if components is None:
            components = ["all"]
        components = as_list(components)
        norm_comps = normalize_components(components)
        for i in norm_comps:
            if self._clients[i] is not None:
                print(self._clients[i])
                result = self._clients[i].connect()
                print(result)

    def connect_all(self):
        self.connect()

    def disconnect(self, components=None):
        if components is None:
            components = ["all"]
        components = as_list(components)
        norm_comps = normalize_components(components)
        for i in norm_comps:
            if self._clients[i] is not None:
                print(self._clients[i])
                result = self._clients[i].disconnect()
                print(result)

    def disconnect_all(self):
        pass

    def getStatus(self):
        pass

    def setCrcRcConfig(self, req):
        pass

    def clearCrcRcConfig(self, req):
        pass

    def clearAllCrcRcConfig(self):
        pass

    def checkAllAlive(self):
        pass

    # # can stack

    def checkAlive(self):
        return self._canstack.checkAlive()

    def getVersion(self):
        return self._canstack.getVersion()

    def setConfigs(self, req):
        return self._canstack.setConfigs(req)

    def start(self):
        return self._canstack.startCanStack()

    def stop(self):
        return self._canstack.stopCanStack()

    def clearCanSend(self):
        return self._canstack.clearCanSend()

    def setCanCrcRcConfig(self, req):
        return self._canstack.setCrcRcConfig(req)

    def clearCanCrcRcConfig(self, req):
        return self._canstack.clearCrcRcConfig(req)

    def clearCanAllCrcRcConfig(self):
        return self._canstack.clearAllCrcRcConfig()

    def sendCanMessageCyc(self, req):
        return self._canstack.sendCanMessageCyc(req)

    def sendCanMessage(self, req):
        return self._canstack.sendCanMessage(req)

    def sendCanMessages(self, req, stmin):
        return self._canstack.sendCanMessages(req, stmin)

    def getStackStatus(self):
        return self._canstack.getStackStatus()

    def stopChannelSendCyc(self, req):
        return self._canstack.stopChannelSendCyc(req)

    def sendCan(self, req):
        return self._canstack.sendCan(req)

    def getChannelBusloadCurrent(self, req):
        return self._canstack.getChannelBusloadCurrent(req)

    def getChannelBusloadMax(self, req):
        return self._canstack.getChannelBusloadMax(req)

    def getChannelBusloadAvg(self, req):
        return self._canstack.getChannelBusloadAvg(req)

    def getChannelErrorFrameTotal(self, req):
        return self._canstack.getChannelErrorFrameTotal(req)

    # # can parser

    def setCanParserCrcRcConfig(self, req):
        pass

    def clearAllCanParserCrcRcConfig(self):
        pass

    def clearCanParserCrcRcConfig(self, req):
        pass

    def sendCanFrameCyc(self, req):
        pass

    def sendCanPduCyc(self, req):
        pass

    def sendCanPduCycList(self, req):
        pass

    def sendCanPdu(self, req):
        pass

    def addDbFile(self, req):
        pass

    def setCanConfig(self, req):
        pass

    def getCanDbConfigs(self):
        pass

    def getCanDbPath(self):
        pass

    def subscribeMsg(self, req):
        pass

    def unSubscribeMsg(self, req):
        pass

    def getCanDbInfo(self):
        pass

    def clear(self):
        pass

    def clearCanStackSubscribe(self):
        pass

    def encodePdu(self, req):
        pass

    def convertCanDbToPy(self, req):
        pass

    def convertCanDbToJson(self, req):
        pass

    def updateCanPdu(self, req):
        pass

    # # lin stack

    def reset(self):
        pass

    def setLinConfig(self, req):
        pass

    def setChannelConig(self, req):
        pass

    def startLinStack(self):
        pass

    def stopLinStack(self):
        pass

    def setMessageSimulation(self, req):
        pass

    def setHeaderSimulation(self, req):
        pass

    def setMessageData(self, req):
        pass

    def getLinStatus(self):
        pass

    def clearLinSubscribe(self):
        pass

    def clearLinSend(self, req):
        pass

    def setLinCrcConfig(self, req):
        pass

    def clearLinCrcConfig(self, req):
        pass

    def getDeltaTime(self):
        pass

    # # lin parser

    def addDbfile(self, req):
        pass

    def setChannelConfig(self, req):
        pass

    def setNodeSimulation(self, req):
        pass

    def setFrameSimulation(self, req):
        pass

    def setFrameData(self, req):
        pass

    def SetSignalData(self, req):
        pass

    def clearCanParserSubscribe(self):
        pass

    def clearDbfile(self):
        pass

    def getLinParserStatus(self):
        pass

    def getLdfJsonTree(self):
        pass

    def convertLinDbToPy(self, req):
        pass

    def convertLinDbToJson(self, req):
        pass

    def setCrcConfig(self, req):
        pass

    def clearCrcConfig(self, req):
        pass


def main():
    print("面板模式说明")


if __name__ == "__main__":
    main()
