'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint16_t sofNr;
  uint16_t time[3];
  uint16_t padding;
} cmdTrefSofSeq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint16_t onOff;
} cmdSoftSyncOnOff;
'''


import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


SOFTSYNC_OFF = 0
SOFTSYNC_ON = 1
SOFTSYNC_NOT_STARTED = 2


class TrefSofSeq(Command):  # 0x4b
    cmd_len = 12
    cmd_num = FiloCommandNumber.TREF_SOFNR
    fmt = "< H 3H H"

    def __init__(self, sofnr, t1, t2, t3, padding):
        self.sofnr = sofnr
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.padding = padding

    def serialize_body(self):
        return struct.pack(self.fmt, self.sofnr, self.t1, self.t2, self.t3,
                           self.padding)


class SoftSyncOnOff(Command):  # 0x4c
    cmd_len = 4
    cmd_num = FiloCommandNumber.SOFTSYNC_ONOFF
    fmt = "< H"

    def __init__(self, onoff):
        self.onoff = onoff

    def serialize_body(self):
        return struct.pack(self.fmt, self.onoff)
