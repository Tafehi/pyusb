#!/usr/bin/python3

import usb.core
import time
import usb.util

VID=0x0781, PID=0x5567 # Add your VID and PID using lsusb in linux
dev = usb.core.find(idVendor=VID, idProduct=PID)
if not dev:
    print("No device has been found :(")
    exit(1)
else:
    print("Yeey. Find a device")
