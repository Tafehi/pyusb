#!/usr/bin/python3

import usb.core
import time
import usb.util

# Add your idVendor and idProduct using lsusb in linux
dev = usb.core.find(idVendor=0xffff, idProduct=0x5678)
conf = dev.get_active_configuration()

def main():
    if not dev:
        print("No device has been found :_(")
    else:
        
        print("Yeepy. Usb device is found :)")
        print(f"The size of the Usb is {dev.get_active_configuration().wTotalLength}")
        time.sleep(5) #TODO change 5 sec. to 5 min.


if __name__ == "__main__":
    main()
