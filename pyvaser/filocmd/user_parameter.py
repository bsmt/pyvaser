'''
typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t userNo;
  uint8_t paramNo;
  uint8_t status;
  uint8_t padding[3];
  uint8_t data[8];
} cmdReadUserParameter;

typedef struct {
  uint8_t cmdLen;
  uint8_t cmdNo;
  uint8_t userNo;
  uint8_t paramNo;
  uint8_t status;
  uint8_t type;
  union {
    struct {
      uint8_t pad[2];
      uint8_t clearBits[8];
      uint8_t setBits[8];
    } typeLicense;
    struct {
      uint8_t pad[2];
      uint8_t hash[16];
    } typeCheck;
  };
} cmdWriteUserParameter;
'''

import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class ReadUserParameter(Command):  # 0x68
    cmd_len = 16
    cmd_num = FiloCommandNumber.READ_USER_PARAMETER
    fmt = "< B B B 3B 8s"

    def __init__(self, user_no, param_no, status, pad1, pad2, pad3, data):
        self.user_no = user_no
        self.param_no = param_no
        self.status = status
        self.pad1 = pad1
        self.pad2 = pad2
        self.pad3 = pad3
        self.data = data

    def serialize_body(self):
        return struct.pack(self.fmt, self.user_no, self.param_no, self.status,
                           self.pad1, self.pad2, self.pad3, self.data)


# ugh union
# TODO: write this
class WriteUserParameter(Command):
    cmd_len = 24
    cmd_num = FiloCommandNumber.READ_USER_PARAMETER
    fmt = "< B B B B"
    fmt_license = "< H 8s 8s"
    fmt_check = "< H 16s"

    @classmethod
    def parse(cls, data):
        pass

    def __init__(self):
        pass

    def serialize_body(self):
        pass
