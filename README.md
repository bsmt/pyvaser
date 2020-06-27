# pyvaser

A very much half-baked pure python USB driver for kvaser CAN adapters.
Only really tested with the Leaf Light but it *might* work with most of their USB stuff.

## But, why? They already provide drivers.

They provide drivers for Windows and Linux, but MacOS and any other platforms are on their own.
Other people have tried making drivers for MacOS (and maybe others), but they're all kernel mode, which is not ideal IMO and can be avoided by using libusb.
Kvaser's drivers also operate in the kernel, but they were kind enough to ship source code with their linux driver, so at least we don't need to reverse engineer anything to make a userland-only version. 
Big up kvaser!
