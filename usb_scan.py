#!/usr/bin/python3

import usb.core
import time
import usb.util

# Add your idVendor and idProduct using lsusb in linux
dev = usb.core.find(idVendor=0x0781, idProduct=0x5567)
if not dev:
    print("No device has been found :(")
    exit(1)
else:

    print("Yeey. Find a device")
