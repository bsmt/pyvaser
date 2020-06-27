'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  channel;
  uint8_t  transId;
  uint8_t  rawMessage[14];
  uint8_t  _padding0;
  uint8_t  flags;
} cmdTxCanMessage;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  channel;
  uint8_t  transId;
  uint16_t time[3];
  uint8_t  flags;               // Flags detected during tx - currently only NERR
  uint8_t  timeOffset;
} cmdTxAck;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  channel;
  uint8_t  transId;
  uint16_t time[3];
  uint16_t padding;
} cmdTxRequest;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class TxCanMessage(Command):  # 0x0d/0x0f
    cmd_len = 20
    cmd_num = (FiloCommandNumber.TX_STD_MESSAGE,
               FiloCommandNumber.TX_EXT_MESSAGE)
    fmt = "< B B 14s B B"

    def __init__(self, channel, trans_id, raw_message, pad, flags):
        self.channel = channel
        self.trans_id = trans_id
        self.raw_message = raw_message
        self.pad = pad
        self.flags = flags

    def serialize_body(self):
        return struct.pack(self.fmt, self.channel, self.trans_id,
                           self.raw_message, self.pad, self.flags)


class TxAck(Command):  # 0x32
    cmd_len = 12
    cmd_num = FiloCommandNumber.TX_ACK
    fmt = "< B B 3H B B"

    def __init__(self, channel, trans_id, t1, t2, t3, flags, time_offset):
        self.channel = channel
        self.trans_id = trans_id
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.flags = flags
        self.time_offset = time_offset

    def serialize_body(self):
        return struct.pack(self.fmt, self.channel, self.trans_id, self.t1,
                           self.t2, self.t3, self.flags, self.time_offset)


class TxRequest(Command):  # 0x3c
    cmd_len = 12
    cmd_num = FiloCommandNumber.TX_REQ
    fmt = "< B B 3H H"

    def __init__(self, channel, trans_id, t1, t2, t3, pad):
        self.channel = channel
        self.trans_id = trans_id
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.pad = pad

    def serialize_body(self):
        return struct.pack(self.fmt, self.channel, self.trans_id, self.t1,
                           self.t2, self.t3, self.pad)
