'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t channel;
} cmdGetBusLoadReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
  uint16_t time[3];             // "Absolute" timestamp
  uint16_t sample_interval;     // Sampling interval in microseconds
  uint16_t active_samples;      // Number of samples where tx or rx was active
  uint16_t delta_t;             // Milliseconds since last response
} cmdGetBusLoadResp;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class GetBusLoadReq(Command):  # 0x28
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_BUSLOAD_REQ
    fmt = "< B B"

    def __init__(self, trans_id, channel):
        self.trans_id = trans_id
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel)


class GetBusLoadResp(Command):  # 0x29
    cmd_len = 16
    cmd_num = FiloCommandNumber.GET_BUSLOAD_RESP
    fmt = "< B B 3H H H H"

    def __init__(self, trans_id, channel, t1, t2, t3, sample_interval,
                 active_samples, delta_t):
        self.trans_id = trans_id
        self.channel = channel
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.sample_interval = sample_interval
        self.active_samples = active_samples
        self.delta_t = delta_t

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel, self.t1,
                           self.t2, self.t3, self.sample_interval,
                           self.active_samples, self.delta_t)
