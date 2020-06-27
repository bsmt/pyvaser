'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  int8_t  dataLevel;
} cmdGetCardInfoReq;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  channelCount;
  uint32_t serialNumber;
  uint32_t padding1;            // Unused right now
  uint32_t clockResolution;
  uint32_t mfgDate;
  // The EAN is encoded into two 32-bit integers in hex, so that
  // 0x00073301 and 0x30002425 gives the ean 0007330130002425
  uint8_t  EAN[8];              // LSB..MSB, then the check digit.
  uint8_t  hwRevision;
  uint8_t  usbHsMode;
  uint8_t  hwType;              // HWTYPE_xxx (only f/w 1.2 and after)
  uint8_t  canTimeStampRef;
} cmdGetCardInfoResp;
'''


import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class GetCardInfoReq(Command):
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_CARD_INFO_REQ  # 0x22
    fmt = "< B b"

    def __init__(self, trans_id, data_level):
        self.trans_id = trans_id
        self.data_level = data_level

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.data_level)


class GetCardInfoResp(Command):
    cmd_len = 32
    cmd_num = FiloCommandNumber.GET_CARD_INFO_RESP  # 0x23
    fmt = "< B B I I I I 8s B B B B"

    def __init__(self, trans_id, channel_count, serial, padding1, clock_res,
                 mfg_date, ean, hw_rev, usb_hd_mode, hw_type, can_timestamp):
        self.trans_id = trans_id
        self.channel_count = channel_count
        self.serial = serial
        self.padding1 = padding1
        self.clock_res = clock_res
        self.mfg_date = mfg_date
        self.ean = ean
        self.hw_rev = hw_rev
        self.usb_hd_mode = usb_hd_mode
        self.hw_type = hw_type
        self.can_timestamp = can_timestamp

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.channel_count,
                           self.serial, self.padding1, self.clock_res,
                           self.mfg_date, self.ean, self.hw_rev,
                           self.usb_hd_mode, self.hw_type,
                           self.can_timestamp)

'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t transId;
  int8_t dataLevel;
} cmdGetCardInfo2Req;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  reserved0;           // Unused right now
  uint8_t  pcb_id[24];
  uint32_t oem_unlock_code;
} cmdGetCardInfo2Resp;
'''

class GetCardInfo2Req(Command):  # 0x20
    cmd_len = 4
    cmd_num = FiloCommandNumber.GET_CARD_INFO_2
    fmt = "< B b"

    def __init__(self, trans_id, data_level):
        self.trans_id = trans_id
        self.data_level = data_level

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.data_level)


class GetCardInfo2Resp(Command):  # 0x20?
    cmd_len = 32
    cmd_num = FiloCommandNumber.GET_CARD_INFO_2
    fmt = "< B B 24s I"

    def __init__(self, trans_id, reserved, pcb_id, oem_unlock_code):
        self.trans_id = trans_id
        self.reserved = reserved
        self.pcb_id = pcb_id
        self.oem_unlock_code = oem_unlock_code

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.reserved,
                           self.pcb_id, self.oem_unlock_code)
