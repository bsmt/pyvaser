'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  uint8_t padding;
} cmdCheckLicenseReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  padding;
  uint32_t licenseMask;
  uint32_t kvaserLicenseMask;
} cmdCheckLicenseResp;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class CheckLicenseReq(Command):  # 0x2b
    cmd_len = 4
    cmd_num = FiloCommandNumber.CHECK_LICENSE_REQ
    fmt = "< B B"

    def __init__(self, trans_id, padding):
        self.trans_id = trans_id
        self.padding = padding

    def serialize_body(self):
        return struct.pack(self.trans_id, self.padding)


class CheckLicenseResp(Command):  # 0x2c
    cmd_len = 12
    cmd_num = FiloCommandNumber.CHECK_LICENSE_RESP
    fmt = "< B B I I"

    def __init__(self, trans_id, padding, license_mask, kvaser_license_mask):
        self.trans_id = trans_id
        self.padding = padding
        self.license_mask = license_mask
        self.kvaser_license_mask = kvaser_license_mask

    def serialize_body(self):
        return struct.pack(self.trans_id, self.padding, self.license_mask,
                           self.kvaser_license_mask)
