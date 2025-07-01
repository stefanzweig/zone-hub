import os
import sys
import time
import typing
from pathlib import Path
from typing import Union, Callable

sys.path.append(".")
try:
    project_root = Path(__file__).resolve().parent.parent
    thrift_dir = project_root / "IDL" / "thrift"
    if not thrift_dir.exists():
        raise FileNotFoundError(f"Thrift目录不存在: {thrift_dir}")

    for path in [project_root, thrift_dir]:
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.append(path_str)
except Exception as e:
    print(f"路径添加失败: {e}")
    raise

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

print(dir())
from utils import *


# APIs for the test suites' development.
def create_can_client():
    pass


def create_canparser_client():
    pass


def create_configs():
    pass


class Foundation(object):
    """
    一个有 49 个操作
    """

    clients = []

    def __init__(self) -> None:
        pass

    def __del__(self):
        pass

    def Subscribe(self, obj) -> None:
        """
        订阅对象事件，只有订阅了相关对象，才能在后续的 OnXXX 回调函数中收到对应的对象接收事件

        :param obj: 需要订阅的对象，可以是如下类型\n
            - CanMessage
            - CanFrame
            - CanSignal
            - CanISignalIPdu
            - SomeipPackage
            - LinMessage
            - LinFrame
            - LinSignal
        """
        pass

    def UnSubscribe(self, obj) -> None:
        """
        取消订阅事件，调用该函数后，将不会再 OnXXX 的回调函数中收到相关消息

        :param obj: 需要取消订阅的对象，可以为如下类型\n
            - CanMessage\n
            - CanFrame\n
            - CanSignal\n
            - CanISignalIPdu\n
            - SomeipPackage\n
        """
        pass

    def OnCanFrame(self, timestamp, can_frame: canMessage) -> None:
        """

        Args:
            timestamp:
            can_frame:

        Returns:

        """
        pass

    def OnCanPdu(self, timestamp, can_pdu: pduMessage) -> None:
        """

        Args:
            timestamp:
            can_pdu:

        Returns:

        """
        pass

    def OnCanSignal(self, timestamp, can_signal: iSignalIPduObj) -> None:
        """

        Args:
            timestamp:
            can_signal:

        Returns:

        """
        pass

    def OnDiagRequest_DoIP(self, diagnostic_request: canMessage):
        """

        Args:
            diagnostic_request:

        Returns:

        """
        pass

    def OnDiagResponse_DoIP(self, diagnostic_response: canMessage):
        """

        Args:
            diagnostic_response:

        Returns:

        """
        pass

    def OnDiagRequest(self, diagnostic_request: canMessage):
        """

        Args:
            diagnostic_request:

        Returns:

        """
        pass

    def OnDiagResponse(self, diagnostic_response: canMessage):
        """

        Args:
            diagnostic_response:

        Returns:

        """
        pass

    def OnCanMessage(self, timestamp, can_message: canMessage) -> None:
        """

        Args:
            timestamp:
            can_message:

        Returns:

        """
        pass

    def OnSomeipPackage(self, timestamp, someip_package: someipPackage) -> None:
        """

        Args:
            timestamp:
            someip_package:

        Returns:

        """
        pass

    def OnSomeipCalling(
        self, timestamp, someip_in: someipPackage, someip_out: someipPackage
    ) -> None:
        """

        Args:
            timestamp:
            someip_in:
            someip_out:

        Returns:

        """
        pass

    def OnSomeipBypass(self, timestamp, someip_package: someipPackage) -> None:
        """

        Args:
            timestamp:
            someip_package:

        Returns:

        """
        pass

    def OnSomeipStateChange(
        self, timestamp, service: tuple, state: int
    ) -> None:
        """

        Args:
            timestamp:
            service:
            state:

        Returns:

        """
        pass

    def OnLinMessage(self, timestamp, lin_message: linMessageDataT) -> None:
        """

        Args:
            timestamp:
            lin_message:

        Returns:

        """
        pass

    def OnLinFrame(self, timestamp, lin_frame: linMessageDataT) -> None:
        """

        Args:
            timestamp:
            lin_frame:

        Returns:

        """
        pass

    def OnLinSignal(self, timestamp, lin_signal: iSignalIPduObj) -> None:
        """

        Args:
            timestamp:
            lin_signal:

        Returns:

        """
        pass

    def SetCrcRcConfig(
        self,
        channel: int,
        pdu: typing.Union[iSignalIPduEncode, str],
        crc: typing.Union[iSignalIPduEncode, str, int],
        rc: typing.Union[iSignalIPduEncode, str, int],
        crc_table: list = None,
        rc_config: tuple = (0, 15, 1),
    ):
        if crc_table is None:
            crc_table = []
        pass

    def ClearCrcRcConfig(
        self,
        channel: int,
        pdu: typing.Union[iSignalIPduEncode, str],
        crc: typing.Union[iSignalIPduEncode, str, int],
        rc: typing.Union[iSignalIPduEncode, str, int],
    ):
        pass

    def SendCan(self, obj: canMessage, **kwargs) -> None:
        """
        发送一条CAN报文, 数据将立刻发送
        Args:
            obj:
            **kwargs:

        Returns:

        """
        pass

    def SendCanPDU(self, obj: pduMessage, **kwargs) -> None:
        """
        发送一条CANPDU报文, 数据将立刻发送
        """
        pass

    def SetPduListCycleSendTask(
        self, period_ms_list: typing.List[int], obj_list: list, **kwargs
    ):
        """ """
        pass

    def SetCycleSendTask(
        self, period_ms: int, obj, times: int, **kwargs
    ) -> None:
        """ """
        pass

    def SomeipCallAsync(
        self, someip_package: someipPackage, *args, **kwargs
    ) -> None:
        """

        Args:
            someip_package:
            *args:
            **kwargs:

        Returns:

        """
        pass

    def SomeipSetDefaultAnswer(self, someip_package: someipPackage) -> None:
        """

        Args:
            someip_package:

        Returns:

        """
        pass

    def SomeipPublish(
        self, someip_package: someipPackage, *args, **kwargs
    ) -> None:
        """

        Args:
            someip_package:
            *args:
            **kwargs:

        Returns:

        """
        pass

    def SetLinData(self, obj):
        """

        Args:
            obj:

        Returns:

        """
        pass

    def diag_request_doip(self, obj):
        """

        Args:
            obj:

        Returns:

        """
        pass

    def diag_response_doip(self, obj):
        """

        Args:
            obj:

        Returns:

        """
        pass

    def diag_request(self, obj):
        """

        Args:
            obj:

        Returns:

        """
        pass

    def diag_response(self, obj):
        """

        Args:
            obj:

        Returns:

        """
        pass

    def _DealWithDoIPUdsMessageRequest(self, recv_d):
        """
        DDS one

        Args:
            recv_d:

        Returns:

        """
        pass

    def _DealWithDoIPUdsMessageResponse(self, recv_d):
        """
        DDS one

        Args:
            recv_d:

        Returns:

        """
        pass

    def _DealWithCanUdsMessageRequest(self, recv_d: dict):
        """
        DDS one

        Args:
            recv_d:

        Returns:

        """
        pass

    def _DealWithCanUdsMessageResponse(self, recv_d: dict):
        """
        DDS one

        Args:
            recv_d:

        Returns:

        """
        pass

    ####dds回调处理函数
    def _DealWithRecvLinFromDDS(self, frames):
        """
        DDS one

        Args:
            frames:

        Returns:

        """
        pass

    def _DealWithRecvSomeipStateFromDDS(self, state):
        """
        DDS one

        Args:
            state:

        Returns:

        """
        pass

    def _DealWithRecvSomeipPackageFromDDS(self, frame):
        """

        Args:
            frame:

        Returns:

        """
        pass

    def _DealWithRecvSomeipCallingFromDDS(self, frame):
        """

        Args:
            frame:

        Returns:

        """
        pass

    def _DealWithRecvSomeipBypassFromDDS(self, frame):
        """

        Args:
            frame:

        Returns:

        """
        pass

    def _DealWithSomeipCalling_(self, recv_d) -> None:
        """

        Args:
            recv_d:

        Returns:

        """
        pass

    def _DealWithRecvCanUdsFromDDS(self, message):
        """

        Args:
            message:

        Returns:

        """
        pass

    def _ddsSomeIpFrameToSomeipPackage(self, SomeIpDatadds):
        """

        Args:
            SomeIpDatadds:

        Returns:

        """
        pass

    def _DealWithRecvCanParserFromDDS(self, frame):
        """

        Args:
            frame:

        Returns:

        """
        pass

    def _DealWithPduFromDDS(self, pdu, frame):
        """

        Args:
            pdu:
            frame:

        Returns:

        """
        pass

    @staticmethod
    def formatPhyValue(input_str: str):
        """

        Args:
            input_str:

        Returns:

        """
        pass

    @staticmethod
    def IsFloatNum(str_in: str):
        """

        Args:
            str_in:

        Returns:

        """
        pass

    @staticmethod
    def IsNegativeIntNum(str_in: str):
        """

        Args:
            str_in:

        Returns:

        """
        pass

    @staticmethod
    def IsNegativeFloatNum(str_in: str):
        pass

    def _DealWithRecvDoIpUdsFromDDS(self, doip_message):
        pass

    # 下面是从framework类拷贝出来，不用继承。
    def Reset(self) -> None:
        pass

    def Reset_LIN(self) -> None:
        pass

    def Reset_CAN(self) -> None:
        pass

    def Reset_SomeIP(self) -> None:
        pass

    def Reset_DoIP(self) -> None:
        pass

    def Reset_XcpOnCan(self) -> None:
        pass


def main():
    print("面板模式说明")


if __name__ == "__main__":
    main()
