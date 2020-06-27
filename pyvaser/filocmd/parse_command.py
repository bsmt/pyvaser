from .get_capabilities import CommandCapabilitiesReq, CommandCapabilitiesResp
from .get_card_info import GetCardInfoReq, GetCardInfoResp, \
    GetCardInfo2Req, GetCardInfo2Resp
from .log_message import LogMessage
from .software_info import GetSoftwareInfoReq, GetSoftwareInfoResp
from .usb_throttle import USBThrottle, USBThrottleScaled
from .check_license import CheckLicenseReq, CheckLicenseResp
from .get_device_name import GetDeviceNameReq, GetDeviceNameResp
from .get_transceiver_info import GetTransceiverInfoReq, GetTransceiverInfoResp
from .misc import Sound
from .bus_params import SetBusParamsReq, GetBusParamsReq, GetBusParamsResp
from .driver_mode import SetDriverModeReq, GetDriverModeReq, GetDriverModeResp
from .user_parameter import ReadUserParameter, WriteUserParameter
from .start_chip import StartChipReq, StartChipResp
from .soft_sync import TrefSofSeq, SoftSyncOnOff
from .chip_state import GetChipStateReq, ChipStateEvent
from .bus_load import GetBusLoadReq, GetBusLoadResp
from .stop_chip import StopChipReq, StopChipResp
from .tx_message import TxCanMessage, TxAck, TxRequest


ALL_CMDS = (CommandCapabilitiesReq, CommandCapabilitiesReq,
            GetCardInfoReq, GetCardInfoResp, GetCardInfo2Req, GetCardInfo2Resp,
            LogMessage,
            GetSoftwareInfoReq, GetSoftwareInfoResp,
            USBThrottle, USBThrottleScaled,
            CheckLicenseReq, CheckLicenseResp,
            GetDeviceNameReq, GetDeviceNameResp,
            GetTransceiverInfoReq, GetTransceiverInfoResp,
            Sound,
            SetBusParamsReq, GetBusParamsReq, GetBusParamsResp,
            SetDriverModeReq, GetDriverModeReq, GetDriverModeResp,
            ReadUserParameter, WriteUserParameter,
            StartChipReq, StartChipResp,
            TrefSofSeq, SoftSyncOnOff,
            GetChipStateReq, ChipStateEvent,
            GetBusLoadReq, GetBusLoadResp,
            StopChipReq, StopChipResp,
            TxCanMessage, TxAck, TxRequest)


def parse_commands(data):
    '''Parse out one (or more) FILO commands from a byte string.'''
    idx = 0
    while idx < len(data):
        size = ord(data[idx])
        packet = data[idx:idx + size]
        yield parse_command(packet)
        idx += size


def parse_command(data):
    _size = data[0]
    cmd = ord(data[1])
    body = data[2:]

    for CommandClass in ALL_CMDS:
        try:
            if cmd in CommandClass.cmd_num:
                return CommandClass.parse(body)
        except TypeError:
            if cmd == CommandClass.cmd_num:
                return CommandClass.parse(body)
