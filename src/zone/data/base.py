from IDL.thrift.CanStackNode.ttypes import (
    canMessage,
    canMessages,
    canChannelConfigs,
    canChannelConfig,
)
from IDL.thrift.CanParserNode.ttypes import (
    canDbInfo,
    pduMessage,
    pduMessages,
    pduUpdate,
    pduCrcRcConfig,
    iSignalIPduEncode,
    iSignalIPduObj,
)
from IDL.thrift.ConfigNode.ttypes import dbPath, canConfigInfo
from IDL.thrift.SomeIpNode.ttypes import (
    someipInfo,
    someipPackage,
    someipServiceInfo,
    someipServiceInfos,
    someipStackConfig,
    someipChannelConfig,
)
from IDL.thrift.LinStackNode.ttypes import (
    linStackStatus,
    linMessageConfig,
    linCrcConfig,
    linHeaderConfig,
    linMessageDataT,
)


class CanMessage(canMessage):
    pass


class CanMessages(canMessages):
    pass


class CanChannelconfigs(canChannelConfigs):
    pass


class CanChannelconfig(canChannelConfig):
    pass


class CanDbinfo(canDbInfo):
    pass


class PduMessage(pduMessage):
    pass


class PduMessages(pduMessages):
    pass


class PduUpdate(pduUpdate):
    pass


class PduCrcRcConfig(pduCrcRcConfig):
    pass


class ISignaliPduEncode(iSignalIPduEncode):
    pass


class ISignaliPduObj(iSignalIPduObj):
    pass


class DbPath(dbPath):
    pass


class CanConfigInfo(canConfigInfo):
    pass


class SomeipInfo(someipInfo):
    pass


class SomeipPackage(someipPackage):
    pass


class SomeipServiceInfo(someipServiceInfo):
    pass


class SomeipServiceInfos(someipServiceInfos):
    pass


class SomeipStackConfig(someipStackConfig):
    pass


class SomeipChannelConfig(someipChannelConfig):
    pass


class LinStackStatus(linStackStatus):
    pass


class LinMessageConfig(linMessageConfig):
    pass


class LinCrcConfig(linCrcConfig):
    pass


class LinHeaderConfig(linHeaderConfig):
    pass


class LinMessageDataT(linMessageDataT):
    pass
