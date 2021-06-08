#!/usr/bin/python3



import usb.core
import time
import usb.util

# Add your idVendor and idProduct using lsusb in linux
dev = usb.core.find(idVendor=0xffff, idProduct=0x5678)

# find our device
def main():
    # was it found?
    if dev is None:
        raise ValueError('Device not found :(')
    else:

    # set the active configuration. With no arguments, the first
    # configuration will be the active one
        print('Device is Found :)')
        #get an endpoint
        # get active configuration
        cfg = dev.get_active_configuration()
        #show the usb size
        print(f"The usb size is {cfg.wTotalLength}")
        #get interface description
        intf = cfg[(0,0)]
        #print(intf)
        #print("=---------------------=====================-----------------")
        # get endpoint 0x1
        ep1 = intf[0]
        #print(ep1)
        # get endpoint 0x82
        ep82 = intf[1]
        time.sleep(5) #TODO change 5 sec. to 5 min.
        #print(ep82)

if __name__ == "__main__":
    main()
