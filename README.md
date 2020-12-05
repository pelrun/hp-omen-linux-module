HP Omen special feature control for Linux
-----------------------------------------

This is a version of the hp-wmi kernel module that implements some of the features of HP Omen Command Centre.

It's totally experimental right now, and could easily crash your machine. As such I'm not going to provide any instructions just yet.

Currently working:

FourZone keyboard colour control (/sys/devices/platforms/hp-wmi/rgb-zones)

## Installation
Run ```make``` inside the module folder.
Require the kernel headers to be installed in order to run.

Then run
```# rmmod hp-wmi```
```# insmod hp-wmi.ko```

The FourZone interface is now up and running

### Usage
The module creates four zones in `/sys/devices/platform/hp-wmi/rgb_zones/` as zoneXX between 00 and 03. 
To use these, just write the hex colour in the RGB format as 0xRRGGBB. e.g.:
`echo 0x00FFFF > /sys/devices/platform/hp-wmi/rgb_zones/zone00` to get sky-blue

### To do:

___FourZone brightness control___ not necessary as brightness is managed from hex values
- GUI
- Fan control 
- Performance level 
- Network booster (?) 
- DKMS module

