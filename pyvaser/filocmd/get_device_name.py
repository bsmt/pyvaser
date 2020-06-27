'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t padding[2];
} cmdGetDeviceNameReq;

typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t index;
  uint8_t padding;
  uint8_t data[16];
} cmdGetDeviceNameResp;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class GetDeviceNameReq(Command):  # 0x77
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_DEVICE_NAME_REQ
    fmt = "< H"

    def __init__(self, padding):
        self.padding = padding

    def serialize_body(self):
        return struct.pack(self.fmt, self.padding)


class GetDeviceNameResp(Command):  # 0x78
    cmd_len = 18
    cmd_num = FiloCommandNumber.GET_DEVICE_NAME_RESP
    fmt = "< B B 16s"

    def __init__(self, index, padding, data):
        self.index = index
        self.padding = pdding
        self.data = data

    def serialize_body(self):
        return struct.pack(self.fmt, self.index, self.padding, self.data)
