# radiopie
A Raspberry Pi web radio client using a vintage two-line LCD screen

## Recommended hardware setup

I built the system using a first generation Model B.
The Raspberry offers both network and sound capabilities,
so you only need a suitable display, depending on your casing and taste.
You can find cheap LCDs in many stores,
e.g. on [ebay](https://www.ebay.com/sch/i.html?_nkw=character+lcd+arduino).

I also recommend the
[PowerBlock](https://blog.petrockblock.com/powerblock-raspberry-pi-power-switch/)
to get feedback on the boot and shutdown process without a proper screen,
and also to be able to turn your radio on and off using a traditional switch.

## Required software

You should proceed through the steps outlined on
[Adafruit](https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black/)
to install the library for controlling the display.
Also, if you chose to use the PowerBlock, you need to install a driver,
which can be found on the page linked above.
