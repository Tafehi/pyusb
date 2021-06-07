import usb.core

dev=usb.core.find(idVendor=0x0781, idProduct=0x5567)
ep = dev[0].interfaces()[0]

