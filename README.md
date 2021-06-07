## Read usb via linux service
- To read all usb devices on Linux use `lsusb` to find Device id
- to read `idVendor` and `idProduct` use  `lsusb -D /dev/bus/usb/001/<Device id>`
![](lsusb.PNG)

## How to run it

1. copy the python code into `/usr/local/bin/`
2. copy the `usb_scan.service` in to `/lib/systemd/system/`
3. Reload the systemctl daemon to read new file. You need to reload this deamon each time after making any changes in in .service file. `$ sudo systemctl daemon-reload`
4. Now enable and start your new service
`$ sudo systemctl enable test-py.service`
`$ sudo systemctl start test-py.service`
5. For service status: `$ sudo systemctl status test-py.service`
Write a Linux service that starts when a USB drive is inserted and implements the following

* clean up files until a configurable amount of free space is available
* clean up by age, delete the oldest files first
* also trigger a cleanup every 5th minute
* Instantly trigger cleanup if drive usage goes above 80%

Use Python for scripting