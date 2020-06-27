'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
  uint32_t bitRate;
  uint8_t  tseg1;
  uint8_t  tseg2;
  uint8_t  sjw;
  uint8_t  noSamp;
} cmdSetBusparamsReq;

typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t channel;
} cmdGetBusparamsReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
  uint32_t bitRate;
  uint8_t  tseg1;
  uint8_t  tseg2;
  uint8_t  sjw;
  uint8_t  noSamp;
} cmdGetBusparamsResp;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class SetBusParamsReq(Command):  # 0x10
    cmd_len = 12
    cmd_num = FiloCommandNumber.SET_BUSPARAMS_REQ
    fmt = "< B B I B B B B"

    def __init__(self, trans_id, channel, bitrate, tseg1, tseg2, sjw, no_samp):
        self.trans_id = trans_id
        self.channel = channel
        self.bitrate = bitrate
        self.tseg1 = tseg1
        self.tseg2 = tseg2
        self.sjw = sjw
        self.no_samp = no_samp

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel, self.bitrate,
                           self.tseg1, self.tseg2, self.sjw, self.no_samp)


class GetBusParamsReq(Command):  # 0x11
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_BUSPARAMS_REQ
    fmt = "< B B"

    def __init__(self, trans_id, channel):
        self.trans_id = trans_id
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel)


class GetBusParamsResp(Command):  # 0x12
    cmd_len = 12
    cmd_num = FiloCommandNumber.GET_BUSPARAMS_RESP
    fmt = "< B B I B B B B"

    def __init__(self, trans_id, channel, bitrate, tseg1, tseg2, sjw, no_samp):
        self.trans_id = trans_id
        self.channel = channel
        self.bitrate = bitrate
        self.tseg1 = tseg1
        self.tseg2 = tseg2
        self.sjw = sjw
        self.no_samp = no_samp

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel, self.bitrate,
                           self.tseg1, self.tseg2, self.sjw, self.no_samp)

