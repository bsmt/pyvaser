'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t channel;
} cmdStopChipReq;

typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t channel;
} cmdStopChipResp;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class StopChipReq(Command):  # 0x1c
    cmd_len = 4
    cmd_num = FiloCommandNumber.STOP_CHIP_REQ
    fmt = "< B B"

    def __init__(self, trans_id, channel):
        self.trans_id = trans_id
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel)


class StopChipResp(Command):  # 0x1d
    cmd_len = 4
    cmd_num = FiloCommandNumber.STOP_CHIP_RESP
    fmt = "< B B"

    def __init__(self, trans_id, channel):
        self.trans_id = trans_id
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel)
