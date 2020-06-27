# pyvaser arduino test jig

So, we have a maybe-working USB driver for the kvaser, but how do we test it?
We could make a test network and connect it to another adapter that we know works,
and use that to see if our commands going to the kvaser are doing what are expected.
*But*, the only other CAN bus adapter I have is the Sparkfun Arduino shield, and I don't want to spend ~$100 for another *decent* CAN controller that I can easily interface with.
So, Arduino it is; on the upside, it'll be easy for other people to reproduce if necessary.

## Kvaser-Arduino Test Network Setup

Note that you *need* 120 ohm terminating resistors when setting up the test network.
Actual accuracy of the resistors doesn't seem to matter that much, 100 ohm worked fine for me. 
I can get away with only putting a single 100 ohm resistor on one end of the network, but ymmv.
The Kvaser Leaf Light v2 I have has a different DB9 pinout from the Sparkfun shield, because reasons.

* Pin 2 on Kvaser DB9 is CAN Low
* Pin 3 on kvaser DB9 is GND
* Pin 7 on kvaser DB9 is CAN High

I just connected those up to headers on the Sparkfun shield, and used its DB9 connector to place the terminating resistor. Pins 3 and 5 on the Sparkfun DB9 should be CAN Hi-Lo.

## Setup the Arduino

Inside the arduino_sketch folder there's an... arduino sketch. Install the [Sparkfun CAN Arduino Library](https://github.com/sparkfun/SparkFun_CAN-Bus_Arduino_Library) before compiling and uploading the sketch.
All the sketch does is send/receive CAN messages over the USB-serial connection back to our test driver.