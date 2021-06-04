HP Omen special feature control for Linux
-----------------------------------------

A version of the hp-wmi kernel module that implements some of the features of HP Omen Command Centre.

This is experimental software and could easily crash your machine.

**USE AT YOUR OWN RISK**

Currently working:

- FourZone keyboard colour control (`/sys/devices/platform/hp-wmi/rgb-zones/zone0[0-3]`)
- Omen hotkeys (<kbd>F14</kbd>-<kbd>F17</kbd>)

## Installation

1. Install dkms and kernel headers

   Ubuntu: these packages are already installed
   
   Arch Linux: `sudo pacman -S dkms linux-headers`

2. Run `sudo make install` inside this project's root directory

   This will build and install the kernel module. DKMS will manage rebuilding it on kernel updates

## Usage

The module creates four files in `/sys/devices/platform/hp-wmi/rgb_zones/` named `zone00 - zone03`.

To change a zone's highlight color, write a hex colour value in RGB format to the respective file. For example,

`sudo bash -c 'echo 00FFFF > /sys/devices/platform/hp-wmi/rgb_zones/zone00'` will change the zone 0 backlight to sky blue.

Hotkeys are bound to regular X11 keysyms:

 - Windows key lock: <kbd>F14</kbd>
 - Omen: <kbd>F15</kbd>
 - <kbd>Fn</kbd>+<kbd>Esc</kbd>: <kbd>F16</kbd>
 - Disable touchpad: <kbd>F17</kbd>

Use your desktop's hotkey manager to assign them to functions like any other key.

## To do

- [ ] FourZone brightness control
- [ ] Fan control 

