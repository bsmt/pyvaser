'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
  uint8_t  driverMode;
  uint8_t  padding;
  uint16_t padding2;
} cmdSetDrivermodeReq;

typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t channel;
} cmdGetDrivermodeReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
  uint8_t  driverMode;
  uint8_t  padding;
  uint16_t padding2;
} cmdGetDrivermodeResp;

#define DRIVERMODE_NORMAL                   0x01
#define DRIVERMODE_SILENT                   0x02
#define DRIVERMODE_SELFRECEPTION            0x03
#define DRIVERMODE_OFF                      0x04
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class SetDriverModeReq(Command):  # 0x15
    cmd_len = 8
    cmd_num = FiloCommandNumber.SET_DRIVERMODE_REQ
    fmt = "< B B B B H"

    def __init__(self, trans_id, channel, driver_mode, padding, padding2):
        self.trans_id = trans_id
        self.channel = channel
        self.driver_mode = driver_mode
        self.padding = padding
        self.padding2 = padding2

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel,
                           self.driver_mode, self.padding, self.padding2)


class GetDriverModeReq(Command):  # 0x16
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_DRIVERMODE_REQ
    fmt = "< B B"

    def __init__(self, trans_id, channel):
        self.trans_id = trans_id
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel)


class GetDriverModeResp(Command):  # 0x17
    cmd_len = 8
    cmd_num = FiloCommandNumber.SET_DRIVERMODE_REQ
    fmt = "< B B B B H"

    def __init__(self, trans_id, channel, driver_mode, padding, padding2):
        self.trans_id = trans_id
        self.channel = channel
        self.driver_mode = driver_mode
        self.padding = padding
        self.padding2 = padding2

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel,
                           self.driver_mode, self.padding, self.padding2)
