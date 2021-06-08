#!/usr/bin/python3



import usb.core
import time
import usb.util

# Add your idVendor and idProduct using lsusb in linux
dev = usb.core.find(idVendor=0xffff, idProduct=0x5678)

# find our device
def main():
    # was it found? :(
    if dev is None:
        raise ValueError('Device not found :(')
    else:


        # Find the device? :)
        print('Device is Found :)')

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
        print(f"Endpoint Address OUT is {ep1.bEndpointAddress}")
        # get endpoint 0x82
        ep82 = intf[1]
        print(f"Endpoint Address IN is {ep82.bEndpointAddress}")
    
        print(ep1)
        print(ep82)
        time.sleep(5) #TODO change 5 sec. to 5 min.
        

if __name__ == "__main__":
    main()


#device = os.popen('sudo blkid').readlines()
#print(device)
#usbs= []
#for u in device:
#    loc = [u.split(':')[0]]
#    if 'dev/sd' not in loc[0]:
#        continue
    
#    loc+=re.findall(r'"["]+"',u)
#    columns = ['loc']+re.findall(r'\b(\w+)=',u)
#    usbs.append(dict(zip(columns,loc)))
#    for u in usbs:
#        print(usb.core.USBTimeoutError)