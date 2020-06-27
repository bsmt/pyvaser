import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command

'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t padding;
} cmdGetSoftwareInfoReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  padding0;
  uint32_t swOptions;
  uint32_t firmwareVersion;
  uint16_t maxOutstandingTx;
  uint16_t padding1;            // Currently unused
  uint32_t padding[4];          // Currently unused
} cmdGetSoftwareInfoResp;
'''


class GetSoftwareInfoReq(Command):  # 0x26
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_SOFTWARE_INFO_REQ
    fmt = "< B B"

    def __init__(self, trans_id, pad):
        self.trans_id = trans_id
        self.pad = pad

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.pad)


class GetSoftwareInfoResp(Command):  # 0x27
    cmd_len = 32
    cmd_num = FiloCommandNumber.GET_SOFTWARE_INFO_RESP
    fmt = "< B B I I H H 4I"

    def __init__(self,trans_id, pad, sw_opts, firmware_ver, max_outstanding_tx,
                 pad1, pad2, pad3, pad4, pad5):
        self.trans_id = trans_id
        self.pad = pad
        self.sw_opts = sw_opts
        self.firmware_version = firmware_ver
        self.max_outstanding_tx = max_outstanding_tx
        self.pad1 = pad1
        self.pad2 = pad2
        self.pad3 = pad3
        self.pad4 = pad4
        self.pad5 = pad5

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.pad, self.sw_opts,
                           self.firmware_version, self.max_outstanding_tx,
                           self.pad1, self.pad2, self.pad3, self.pad4,
                           self.pad5)
