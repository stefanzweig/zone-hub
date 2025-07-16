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

class SomeipInfo(someipInfo):
    pass