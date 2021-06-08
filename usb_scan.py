#!/usr/bin/python3


import time, os

# Add your idVendor and idProduct using lsusb in linux
#dev = usb.core.find(idVendor=0xffff, idProduct=0x5678)
#unmount for test
while(True):
    print("Unmount for testing purposes")
    os.system('sudo mount /mnt')
    # mount the usb drive to root
    print("Mount the usb")
    os.system('sudo mount /dev/sdb1 /mnt')
    print("Search inside the USB and sort the file from newest to the oldest")

    os.system('ls -lht /mnt')
    AvaliableSpace = os.popen("df -Ph /mnt/ | tail -1 | awk '{print $4}'").read()
    print(" ")
    print(f"The avaliable space in USB drive is: {AvaliableSpace}")
    Used = os.popen("df -Ph /mnt/ | tail -1 | awk '{print $5}'").read()
    #print(f"The used space in USB drive is: {Used}")
    Nr = os.popen('ls -l | wc -l').read() 
    print(f"Number of the files in this folder is: {Nr}")
    Used=(int(Used[0]))
    if Used > 80:
        print("The used space is higher than 80%")
        print("The folders in below are older than 5 days. So remove them automatically")
        os.system('find /mnt/ -type f -mtime +30 -print')
        os.system('find /mnt/ -type f -mtime +30 -delete')
    else:
        Used = os.popen("df -Ph /mnt/ | tail -1 | awk '{print $5}'").read()
        print(f"The used space is less than 80% and it is equal to: {Used} ")
    

    time.sleep(5) #TODO change 5 sec. to 5 min. -> (5*60)
            

