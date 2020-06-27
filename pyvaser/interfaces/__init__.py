'''Interface base class that you subclass to implement an actual device.'''

KVASER_USB_VENDOR_ID = 0x0bfd


class KvaserInterface(object):
    @classmethod
    def find(cls):
        '''Look for a Kvaser interface that this class supports'''
        pass

    def __init__(self, dev, bitrate, channel, timeout=30):
        self.dev = dev
        self.bitrate = bitrate
        self.channel = channel
        self.timeout = timeout

    def init_device(self):
        '''Do whatever setup communication the device needs.'''
        pass

    def can_tx(self, can_id, data):
        '''Send a CAN message'''
        pass
