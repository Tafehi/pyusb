## Read usb via linux service
- To read all usb devices on Linux use `lsusb` to find Device id
- to read `idVendor` and `idProduct` use  `lsusb -D /dev/bus/usb/001/<Device id>`
![](lsusb.PNG)
Write a Linux service that starts when a USB drive is inserted and implements the following

* clean up files until a configurable amount of free space is available
* clean up by age, delete the oldest files first
* also trigger a cleanup every 5th minute
* Instantly trigger cleanup if drive usage goes above 80%

Use Python for scripting