'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t channel;
} cmdGetChipStateReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
  uint16_t time[3];
  uint8_t  txErrorCounter;
  uint8_t  rxErrorCounter;
  uint8_t  busStatus;
  uint8_t  padding;
  uint16_t padding2;
} cmdChipStateEvent;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class GetChipStateReq(Command):  # 0x13
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_CHIP_STATE_REQ
    fmt = "< B B"

    def __init__(self, trans_id, channel):
        self.trans_id = trans_id
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel)


class ChipStateEvent(Command):  # 0x14
    cmd_len = 16
    cmd_num = FiloCommandNumber.CHIP_STATE_EVENT
    fmt = "< B B 3H B B B B H"

    def __init__(self, trans_id, channel, t1, t2, t3, tx_err_cnt, rx_err_cnt,
                 bus_status, pad1, pad2):
        self.trans_id = trans_id
        self.channel = channel
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.tx_err_cnt = tx_err_cnt
        self.rx_err_cnt = rx_err_cnt
        self.bus_status = bus_status
        self.pad1 = pad1
        self.pad2 = pad2


    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel, self.t1,
                           self.t2, self.t3, self.tx_err_cnt, self.rx_err_cnt,
                           self.bus_status, self.pad1, self.pad2)
