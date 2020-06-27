'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  channel;
  uint8_t  flags;
  uint16_t time[3];
  uint8_t  rawMessage[14];
} cmdRxCanMessage;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class RxCanMessage(Command):  # 0x0c/0x0e
    cmd_len = 24
    cmd_num = (FiloCommandNumber.RX_STD_MESSAGE,
               FiloCommandNumber.RX_EXT_MESSAGE)
    fmt = "< B B 3H 14s"

    def __init__(self, channel, flags, t1, t2, t3, raw_message):
        self.channel = channel
        self.flags = flags
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.raw_message = raw_message

    def serialize_body(self):
        return struct.pack(self.fmt, self.channel, self.flags, self.t1,
                           self.t2, self.t3, self.raw_message)
