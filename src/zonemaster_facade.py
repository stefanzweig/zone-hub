import os
import sys
import time
from pathlib import Path
from .utils import *
from typing import Union, Callable

sys.path.append(".")


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
        pass

    def UnSubscribe(self, obj) -> None:
        pass

    def OnCanFrame(self, timestamp, can_frame) -> None:
        """

        Args:
            timestamp:
            can_frame:

        Returns:

        """
        pass

    def OnCanPdu(self, timestamp, can_pdu) -> None:
        """

        Args:
            timestamp:
            can_pdu:

        Returns:

        """
        pass

    def OnCanSignal(self, timestamp, can_signal) -> None:
        """

        Args:
            timestamp:
            can_signal:

        Returns:

        """
        pass

    def OnDiagRequest_DoIP(self, diagnostic_request):
        """

        Args:
            diagnostic_request:

        Returns:

        """
        pass

    def OnDiagResponse_DoIP(self, diagnostic_response):
        """

        Args:
            diagnostic_response:

        Returns:

        """
        pass

    def OnDiagRequest(self, diagnostic_request):
        """

        Args:
            diagnostic_request:

        Returns:

        """
        pass

    def OnDiagResponse(self, diagnostic_response):
        """

        Args:
            diagnostic_response:

        Returns:

        """
        pass

    def OnCanMessage(self, timestamp, can_message) -> None:
        """

        Args:
            timestamp:
            can_message:

        Returns:

        """
        pass

    def OnSomeipPackage(self, timestamp, someip_package) -> None:
        """

        Args:
            timestamp:
            someip_package:

        Returns:

        """
        pass

    def OnSomeipCalling(self, timestamp, someip_in, someip_out) -> None:
        """

        Args:
            timestamp:
            someip_in:
            someip_out:

        Returns:

        """
        pass

    def OnSomeipBypass(self, timestamp, someip_package) -> None:
        """

        Args:
            timestamp:
            someip_package:

        Returns:

        """
        pass

    def OnSomeipStateChange(self, timestamp, service, state) -> None:
        """

        Args:
            timestamp:
            service:
            state:

        Returns:

        """
        pass

    def OnLinMessage(self, timestamp, lin_message) -> None:
        """

        Args:
            timestamp:
            lin_message:

        Returns:

        """
        pass

    def OnLinFrame(self, timestamp, lin_frame) -> None:
        """

        Args:
            timestamp:
            lin_frame:

        Returns:

        """
        pass

    def OnLinSignal(self, timestamp, lin_signal) -> None:
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
        pdu,
        crc,
        rc,
        crc_table=None,
        rc_config=(0, 15, 1),
    ):
        if crc_table is None:
            crc_table = []
        pass

    def ClearCrcRcConfig(
        self,
        channel,
        pdu,
        crc,
        rc,
    ):
        pass

    def SendCan(self, obj, **kwargs) -> None:
        pass

    def SetPduListCycleSendTask(self, period_ms_list, obj_list, **kwargs):
        pass

    def SetCycleSendTask(self, period_ms, obj, times, **kwargs) -> None:
        pass

    def SomeipCallAsync(self, someip_package, *args, **kwargs) -> None:
        pass

    def SomeipSetDefaultAnswer(self, someip_package) -> None:
        pass

    def SomeipPublish(self, someip_package, *args, **kwargs) -> None:
        pass

    def SetLinData(self, obj):
        pass

    def diag_request_doip(self, obj):
        pass

    def diag_response_doip(self, obj):
        pass

    def diag_request(self, obj):
        pass

    def diag_response(self, obj):
        pass

    def _DealWithDoIPUdsMessageRequest(self, recv_d):
        pass

    def _DealWithDoIPUdsMessageResponse(self, recv_d):
        pass

    def _DealWithCanUdsMessageRequest(self, recv_d: dict):
        pass

    def _DealWithCanUdsMessageResponse(self, recv_d: dict):
        pass

    ####dds回调处理函数
    def _DealWithRecvLinFromDDS(self, frames):
        pass

    def _DealWithRecvSomeipStateFromDDS(self, state):
        pass

    def _DealWithRecvSomeipPackageFromDDS(self, frame):
        pass

    def _DealWithRecvSomeipCallingFromDDS(self, frame):
        pass

    def _DealWithRecvSomeipBypassFromDDS(self, frame):
        pass

    def _DealWithSomeipCalling_(self, recv_d) -> None:
        pass

    def _DealWithRecvCanUdsFromDDS(self, message):
        pass

    def _ddsSomeIpFrameToSomeipPackage(self, SomeIpDatadds):
        pass

    def _DealWithRecvCanParserFromDDS(self, frame):
        pass

    def _DealWithPduFromDDS(self, pdu, frame):
        pass

    @staticmethod
    def formatPhyValue(input_str: str):
        pass

    @staticmethod
    def IsFloatNum(str_in: str):
        pass

    @staticmethod
    def IsNegativeIntNum(str_in: str):
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
