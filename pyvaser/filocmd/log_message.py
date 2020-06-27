'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  channel;
  uint8_t  flags;               // MSGFLAG_*
  uint16_t time[3];  // measured in "ticks"
  uint8_t  dlc;
  uint8_t  timeOffset;
  uint32_t id;                  // incl. CAN_IDENT_IS_EXTENDED
  uint8_t  data[8];
} cmdLogMessage;
'''


import struct


from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class LogMessage(Command):
    cmd_len = 24
    cmd_num = FiloCommandNumber.LOG_MESSAGE
    fmt = "< B B 3H B B I 8s"

    def __init__(self, channel, flags, t0, t1, t2, dlc, time_offset, log_id,
                 data):
        self.channel = channel
        self.flags = flags
        self.t0 = t0
        self.t1 = t1
        self.t2 = t2
        self.dlc = dlc
        self.time_offset = time_offset
        self.log_id = log_id
        self.data = data

    def serialize_body(self):
        t0 = self.time >> 32
        t1 = (self.time >> 16) & 0xffff
        t2 = self.time & 0xffff
        return struct.pack(self.fmt, self.channel, self.flags, self.t0,
                           self.t1, self.t2, self.dlc, self.time_offset,
                           self.log_id, self.data)
