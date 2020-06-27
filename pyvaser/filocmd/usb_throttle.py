'''
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint16_t throttle;
} cmdUsbThrottle;

#define THROTTLE_FLAG_READ                     1
#define THROTTLE_FLAG_WRITE                    2
typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint16_t throttle;
  uint32_t flag;
} cmdUsbThrottleScaled;
'''


from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command


class USBThrottle(Command):  #0x4d
    cmd_len = 4
    cmd_num = FiloCommandNumber.USB_THROTTLE
    fmt = "< H"

    def __init__(self, throttle):
        self.throttle = throttle

    def serialize_body(self):
        return struct.pack(self.fmt, self.throttle)


class USBThrottleScaled(Command):  # 0x52
    cmd_len = 8
    cmd_num = FiloCommandNumber.USB_THROTTLE_SCALED
    fmt = "< H I"

    def __init__(self, throttle, flag):
        self.throttle = throttle
        self.flag = flag

    def serialize_body(self):
        return struct.pack(self.fmt, self.throttle, self.flag)
