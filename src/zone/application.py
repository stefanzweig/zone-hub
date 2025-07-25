import os
import sys
import time
import typing
from pathlib import Path
from typing import Union, Callable

from zone.IDL.thrift.CanParserNode.ttypes import *
from zone.IDL.thrift.CanStackNode.ttypes import *
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


class canconfig_user(dbConfigs, canChannelConfigs):
    def __init__(self):
        super(canconfig_user, self).__init__()


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
        results = {}
        for i in norm_comps:
            if self._clients[i] is not None:
                print(self._clients[i])
                result = self._clients[i].connect()
                print(result)
                results[i] = result
        return results

    def connect_all(self):
        return self.connect()

    def disconnect(self, components=None):
        if components is None:
            components = ["all"]
        components = as_list(components)
        norm_comps = normalize_components(components)
        results = {}
        for i in norm_comps:
            if self._clients[i] is not None:
                print(self._clients[i])
                result = self._clients[i].disconnect()
                print(result)
                results[i] = result
        return results

    def disconnect_all(self):
        return self.disconnect()

    def getStatus(self, components=None):
        if components is None:
            components = ["all"]
        components = as_list(components)
        norm_comps = normalize_components(components)
        results = {}
        for i in norm_comps:
            if self._clients[i] is not None:
                print(self._clients[i])
                result = self._clients[i].getStatus()
                print(result)
                results[i] = result
        return results

    def setCrcRcConfig(self, req):
        # canstack and canparser
        # todo
        pass

    def clearCrcRcConfig(self, req):
        # canstack and canparser
        # todo
        pass

    def clearAllCrcRcConfig(self):
        # canstack and canparser
        # todo
        pass

    def checkAlive(self, components=None):
        if components is None:
            components = ["all"]
        components = as_list(components)
        norm_comps = normalize_components(components)
        results = {}
        for i in norm_comps:
            if self._clients[i] is not None:
                print(self._clients[i])
                result = self._clients[i].checkAlive()
                print(result)
                results[i] = result
        return results

    def start(self, components=None):
        if components is None:
            components = ["all"]
        components = as_list(components)
        norm_comps = normalize_components(components)
        results = {}
        for i in norm_comps:
            if self._clients[i] is not None:
                if hasattr(self._clients[i], "start") and callable(
                    getattr(self._clients[i], "start")
                ):
                    result = self._clients[i].start()
                    results[i] = result
        return results

    def stop(self, components=None):
        if components is None:
            components = ["all"]
        components = as_list(components)
        norm_comps = normalize_components(components)
        results = {}
        for i in norm_comps:
            if self._clients[i] is not None:
                if hasattr(self._clients[i], "stop") and callable(
                    getattr(self._clients[i], "stop")
                ):
                    result = self._clients[i].checkAlive()
                    results[i] = result
        return results

    # # can stack

    def getVersion(self):
        return self._canstack.getVersion()

    def setCanConfig(self, req:canconfig_user):
        """pass"""
        self._canparser.setCanConfig()
        self._canstack.setConfigs()

    class canpdu_user(pduMessage, pduUpdate) :
        def __init__(self):
            super().__init__()
    req =    canpdu_user()
    req.channel = 1
    req.pduName = 'test'
    req.period = 100
    req.context = {'sig1:1,sig2:2'}
    req.times = -1
    def sendCanPdu(self,req:canpdu_user):
        self._canparser.updateCanPdu(req)
        self._canparser.sendCanPduCyc(req)

    req.times=0
    def stopCanPdu(self,req:canpdu_user):
        self._canparser.sendCanPduCyc(req)

    def setConfigs(self, dbconfig_user):
        return self._canstack.setConfigs(dbconfig_user)

    def startCanStack(self):
        return self._canstack.startCanStack()

    def stopCanStack(self):
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
        return self._canstack.getStatus()

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
        return self._canparser.setCanParserCrcRcConfig(req)

    def clearAllCanParserCrcRcConfig(self):
        return self._canparser.clearAllCanParserCrcRcConfig()

    def clearCanParserCrcRcConfig(self, req):
        return self._canparser.clearCanParserCrcRcConfig(req)

    def sendCanFrameCyc(self, req):
        return self._canparser.sendCanFrameCyc(req)

    def sendCanPduCyc(self, req):
        return self._canparser.sendCanPduCyc(req)

    def sendCanPduCycList(self, req):
        return self._canparser.sendCanPduCycList(req)

    def sendCanPdu(self, req):
        return self._canparser.sendCanPdu(req)

    def addDbFile(self, req):
        return self._canparser.addDbFile(req)

    def setCanConfig(self, req):
        return self._canparser.setCanConfig(req)

    def getCanDbConfigs(self):
        return self._canparser.getCanDbConfigs()

    def getCanDbPath(self):
        return self._canparser.getCanDbPath()

    def subscribeMsg(self, req):
        return self._canparser.subscribeMsg(req)

    def unSubscribeMsg(self, req):
        return self._canparser.unSubscribeMsg(req)

    def getCanDbInfo(self):
        return self._canparser.getCanDbInfo()

    def clear(self):
        return self._canparser.clear()

    def clearCanStackSubscribe(self):
        return self._canparser.clearCanStackSubscribe()

    def encodePdu(self, req):
        return self._canparser.encodePdu(req)

    def convertCanDbToPy(self, req):
        return self._canparser.convertCanDbToPy(req)

    def convertCanDbToJson(self, req):
        return self._canparser.convertCanDbToJson(req)

    def updateCanPdu(self, req):
        return self._canparser.updateCanPdu(req)

    # # lin stack

    def reset(self):
        return self._linstack.reset()

    def setLinConfig(self, req):
        return self._linstack.setLinConfig(req)

    def setChannelConig(self, req):
        return self._linstack.setChannelConig(req)

    def startLinStack(self):
        return self._linstack.startLinStack()

    def stopLinStack(self):
        return self._linstack.stopLinStack()

    def setMessageSimulation(self, req):
        return self._linstack.setMessageSimulation(req)

    def setHeaderSimulation(self, req):
        return self._linstack.setHeaderSimulation(req)

    def setMessageData(self, req):
        return self._linstack.setMessageData(req)

    def getLinStatus(self):
        return self._linstack.getLinStatus()

    def clearLinSubscribe(self):
        return self._linstack.clearLinSubscribe()

    def clearLinSend(self, req):
        return self._linstack.clearLinSend()

    def setLinCrcConfig(self, req):
        return self._linstack.clearLinSend(req)

    def clearLinCrcConfig(self, req):
        return self._linstack.clearLinCrcConfig(req)

    def getDeltaTime(self):
        return self._linstack.getDeltaTime()

    # # lin parser

    def addDbfile(self, req):
        return self._linparser.addDbfile(req)

    def setChannelConfig(self, req):
        return self._linparser.setChannelConfig(req)

    def setNodeSimulation(self, req):
        return self._linparser.setNodeSimulation(req)

    def setFrameSimulation(self, req):
        return self._linparser.setFrameSimulation(req)

    def setFrameData(self, req):
        return self._linparser.setFrameData(req)

    def SetSignalData(self, req):
        return self._linparser.SetSignalData(req)

    def clearCanParserSubscribe(self):
        return self._linparser.clearCanParserSubscribe()

    def clearDbfile(self):
        return self._linparser.clearDbfile()

    def getLinParserStatus(self):
        return self._linparser.getLinParserStatus()

    def getLdfJsonTree(self):
        return self._linparser.getLdfJsonTree()

    def convertLinDbToPy(self, req):
        return self._linparser.convertLinDbToPy(req)

    def convertLinDbToJson(self, req):
        return self._linparser.convertLinDbToJson(req)

    def setCrcConfig(self, req):
        return self._linparser.setCrcConfig(req)

    def clearCrcConfig(self, req):
        return self._linparser.clearCrcConfig(req)


def main():
    print("面板模式说明")


if __name__ == "__main__":
    main()
