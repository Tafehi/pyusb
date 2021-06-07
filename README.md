## Read usb via linux service
- To read all usb devices on Linux use `lsusb`
Write a Linux service that starts when a USB drive is inserted and implements the following

* clean up files until a configurable amount of free space is available
* clean up by age, delete the oldest files first
* also trigger a cleanup every 5th minute
* Instantly trigger cleanup if drive usage goes above 80%

Use Python for scripting