import random

import usb.core

from pyvaser import filocmd
from pyvaser.filocmd.parse_command import parse_commands
from pyvaser.interfaces import KvaserInterface, KVASER_USB_VENDOR_ID


USB_LEAF_DEVEL_PRODUDCT_ID          = 0x000a
USB_LEAF_LITE_PRODUCT_ID            = 0x000b
USB_LEAF_PRO_PRODUCT_ID             = 0x000c
USB_LEAF_SPRO_PRODUCT_ID            = 0x000e
USB_LEAF_PRO_LS_PRODUCT_ID          = 0x000f
USB_LEAF_PRO_SWC_PRODUCT_ID         = 0x0010
USB_LEAF_PRO_LIN_PRODUCT_ID         = 0x0011
USB_LEAF_SPRO_LS_PRODUCT_ID         = 0x0012
USB_LEAF_SPRO_SWC_PRODUCT_ID        = 0x0013
USB_MEMO2_DEVEL_PRODUCT_ID          = 0x0016
USB_MEMO2_HSHS_PRODUCT_ID           = 0x0017
USB_UPRO_HSHS_PRODUCT_ID            = 0x0018
USB_LEAF_LITE_GI_PRODUCT_ID         = 0x0019
USB_LEAF_PRO_OBDII_PRODUT_ID        = 0x001a
USB_MEMO2_HSLS_PRODUCT_ID           = 0x001b
USB_LEAF_LITE_CH_PRODUCT_ID         = 0x001c
USB_BLACKBIRD_SPRO_PRODUCT_ID       = 0x001d
USB_MEMO_R_SPRO_PRODUCT_ID          = 0x0020
USB_OEM_MERCURY_PRODUCT_ID          = 0x0022
USB_OEM_LEAF_PRODUCT_ID             = 0x0023
USB_OEM_KEY_DRIVING_PRODUCT_ID      = 0x0026
USB_CAN_R_PRODUCT_ID                = 0x0027
USB_LEAF_LITE_V2_PRODUCT_ID         = 0x0120
USB_MINI_PCI_EXPRESS_HS_PRODUCT_ID  = 0x0121
USB_LEAF_LIGHT_HS_V2_OEM_PRODUCT    = 0x0122
USB_USBCAN_LIGHT_2HS_PRODUCT_ID     = 0x0123
USB_MINI_PCI_EXPRESS_2HS_PRODUCT_ID = 0x0124
USB_USBCAN_R_V2_PRODUCT_ID          = 0x0125
USB_LEAF_LITE_R_V2_PRODUCT_ID       = 0x0126
USB_OEM_ATI_LEAF_LITE_V2_PRODUCT_ID = 0x0127

SUPPORTED_DEVICES = (USB_LEAF_LITE_V2_PRODUCT_ID,)


def __filter_device(dev):
    '''Return true if this USB device is supported'''
    if dev.idVendor != KVASER_USB_VENDOR_ID:
        return False
    else:
        if dev.idProduct in SUPPORTED_DEVICES:
            return True
        else:
            return False


class LeafInterface(KvaserInterface):
    @classmethod
    def find(cls, bitrate=500000, channel=0):
        dev = usb.core.find(find_all=True, custom_match=__filter_device)
        for d in dev:
            if d:
                return LeafInterface(d, bitrate=bitrate, channel=channel)
            else:
                return None

    def __init__(self, dev, bitrate=500000, channel=0, timeout=30):
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)
        #usb.util.claim_interface(dev, 0)

        dev.set_configuration()
        cfg = dev.get_active_configuration()
        intf = cfg[(0,0)]
        self.out_ep = usb.util.find_descriptor(
            intf,
            custom_match = \
            lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT)
        self.in_ep = usb.util.find_descriptor(
            intf,
            custom_match = \
            lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_IN)

        self._calc_timing()
        super(LeafInterface, self).__init__(dev, bitrate, channel, timeout)

    def _calc_timing(self):
        '''Kvaser's software can calculate this for any bitrate.
        We're just hardcoding some values for common bitrates.
        The sampling point used for all of them is 75%.'''
        kbits = self.bitrate / 1000
        if kbits == 1000:
            self.tseg1 = 5
            self.tseg2 = 2
            self.sjw = 2
        elif kbits == 500 or kbits == 250 or kbits == 125 or kbits == 83.333 or kbits == 62.5:
            self.tseg1 = 11
            self.tseg2 = 4
            self.sjw = 4
        elif kbits == 100 or kbits == 50 or kbits == 33.333:
            self.tseg1 = 14
            self.tseg2 = 5
            self.sjw = 4
        else:
            raise ValueError("Unknown bitrate. Cannot configure timing.")

    def _usb_send(self, data):
        return self.out_ep.write(data, self.timeout)

    def _usb_receive(self):
        data = self.in_ep.read(self.in_ep.wMaxPacketSize, self.timeout)
        return data.tobytes()

    def do_transaction(self, cmd):
        '''Used for commands that return a specific response,
        and have a transaction id.'''
        trans_id = random.randint(0,255)
        cmd.trans_id = trans_id

        self._usb_send(cmd.serialize())
        recv = self._usb_receive()
        recv_cmds = parse_commands(recv)
        for cmd in recv_cmds:
            if hasattr(cmd, "trans_id"):
                if cmd.trans_id == trans_id:
                    print(cmd)
                    return cmd

    def init_device(self):
        # req card info (transaction)
        #self.do_transaction(filocmd.GetCardInfoReq(0x22, 0x68))
        # set bus params (transaction)
        self.do_transaction(filocmd.SetBusParamsReq(0x00, self.channel,
                                                    self.bitrate, self.tseg1,
                                                    self.tseg2, self.sjw, 1))
        # set driver mode
        self.do_transaction(filocmd.SetDriverModeReq(0x00, self.channel,
                                                     0x01, 0xff, 0xffff))
        # start CAN transceiver (transaction)
        self.do_transaction(filocmd.StartChipReq(0x00, self.channel))

    def stop_device(self):
        self.do_transaction(filocmd.StopChipReq(0x00, self.channel))

    def can_tx(self, id, message):
        '''ID as an int, message as bytes'''
        filocmd.TxCanMessage(self.channel, 0x01, )
        pass

    def can_rx(self):
        '''Blocks until it sees a CAN message'''
        # the leaf sends CAN rx messages as LogMessage, not RxCanMessage...
        pass