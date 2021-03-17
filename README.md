HP Omen special feature control for Linux
-----------------------------------------

This is a version of the hp-wmi kernel module that implements some of the features of HP Omen Command Centre.

It's totally experimental right now, and could easily crash your machine. 

**USE AT YOUR OWN RISK**

Currently working:

- FourZone keyboard colour control (`/sys/devices/platforms/hp-wmi/rgb-zones/zone0[0-3]`)
- Omen key calls calculator

## Installation

1. Install kernel development kit.

1. Run `make` inside the module folder.

1. Then run as root
   ```
   rmmod hp-wmi
   insmod hp-wmi.ko
   ```

The FourZone interface is now up and running

## Usage

The module creates four files in `/sys/devices/platform/hp-wmi/rgb_zones/` named `zone00 - zone03`.

To change zone highlight color, just print hex colour value in RGB format to the respective file. e.g:

`sudo bash -c 'echo 00FFFF > /sys/devices/platform/hp-wmi/rgb_zones/zone00'` to get sky-blue zone 0.

## To do:

- [x] ~~FourZone brightness control~~ not necessary as brightness is managed from hex values
- [ ] Fix bug when pressing calculator key produces hundreds of `XF86Calculator` keyboard events
- [ ] Better utilization of Omen key
- [ ] DKMS module
- [ ] Fan control 
- [ ] Performance level 
- [ ] Network booster (?) 

