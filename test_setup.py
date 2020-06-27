import binascii

from pyvaser.interfaces.leaf import LeafInterface

interface = LeafInterface.find(500000)
interface.init_device()



print(interface.usb_send(b"\x04\x22\x2f\x68"))

print(binascii.hexlify(interface.usb_receive()))
print(binascii.hexlify(interface.usb_receive()))
print(binascii.hexlify(interface.usb_receive()))


#interface.dev.reset()
