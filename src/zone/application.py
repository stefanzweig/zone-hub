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
            "CanStack": self._canstack,
            "CanParser": self._canparser,
            "LinStack": self._linstack,
            "LinParser": self._linparser,
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

    def set_CAN_config(self, config):
        pass

    def set_LIN_config(self, config):
        pass

    def send_CAN(self, message):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def reset(self):
        pass


def main():
    print("面板模式说明")


if __name__ == "__main__":
    main()
