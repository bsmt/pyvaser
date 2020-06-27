import struct

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint8_t  transId;
  uint8_t  subCmd;
  uint16_t freq;
  uint16_t duration;
  uint32_t padding[2];
}  cmdSound;
'''
class Sound(Command):  # 0x4e
    cmd_len = 16
    cmd_num = FiloCommandNumber.SOUND
    fmt = "< B B H H 2I"

    def __init__(self, trans_id, sub_cmd, freq, duration, padding1, padding2):
        self.trans_id = trans_id
        self.sub_cmd = sub_cmd
        self.freq = freq
        self.duration = duration
        self.padding1 = padding1
        self.padding2 = padding2

    def serialize_body(self):
        return struct.pack(self.fmt, self.trans_id, self.sub_cmd, self.freq,
                           self.duration, self.padding1, self.padding2)
