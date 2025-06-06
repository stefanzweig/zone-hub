import sys, os ,logging
import time, json, traceback

sys.path.append('.')
sys.path.append('..')

from IDL.thrift.gen.CanStackNode.canStackNode import canMessage

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from typing import Union
import functools




if __name__ == "__main__":
    pass