#!/usr/bin/python3

import usb.core
import time
import usb.util

# Add your idVendor and idProduct using lsusb in linux
dev = usb.core.find(idVendor=0x0781, idProduct=0x5567)


def main():
    if not dev:
        print("No device has been found :_(")
    else:

        print("Yeey. Find a device")
        time.sleep(5 * 60)


if __name__ == "__main__":
    main()
