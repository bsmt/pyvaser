'''Command superclass'''

import struct


class Command(object):
    cmd_len = 0x00
    cmd_num = 0x00
    fmt = ""

    @classmethod
    def parse(cls, data):
        '''Create a command object from a byte string'''
        args = struct.unpack(cls.fmt, data)
        return cls(*args)

    def serialize_header(self):
        return struct.pack("BB", self.cmd_len, self.cmd_num)

    def serialize(self):
        return self.serialize_header() + self.serialize_body()

    # your subclasses need to implement these two:
    def serialize_body(self):
        '''Serialize the command's data to bytes.'''
        return b""
