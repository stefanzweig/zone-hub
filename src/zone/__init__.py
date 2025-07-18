import sys

from zone.version import get_version
from zone.application import App
from zone import dsc as Data
from zone.utils.config import (
    CAN_Config,
    LIN_Config,
    ETH_Config_PC,
    ETH_Config_Vector,
)


__all__ = ["App"]
__version__ = get_version()
