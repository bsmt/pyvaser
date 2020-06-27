'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
} cmdGetTransceiverInfoReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channel;
  uint32_t transceiverCapabilities;
  uint8_t  transceiverStatus;
  uint8_t  transceiverType;
  uint8_t  padding[2];
} cmdGetTransceiverInfoResp;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class GetTransceiverInfoReq(Command):  # 0x61
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_TRANSCEIVER_INFO_REQ
    fmt = "< B B"

    def __init__(self, trans_id, channel):
        self.trans_id = trans_id
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel)


class GetTransceiverInfoResp(Command):  # 0x62
    cmd_len = 12
    cmd_num = FiloCommandNumber.GET_TRANSCEIVER_INFO_RESP
    fmt = "< B B I B B H"

    def __init__(self, trans_id, channel, trans_caps, trans_status,
                 trans_type, padding):
        self.trans_id = trans_id
        self.channel = channel
        self.transceiver_capabilities = trans_caps
        self.transceiver_status = trans_status
        self.transceiver_type = trans_type
        self.padding = padding

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel,
                           self.transceiver_capabilities,
                           self.transceiver_status,
                           self.transceiver_type,
                           self.padding)
