** THE HARDWARE IS CURRENTLY NOT TESTED **

# Kryptokrona mini miner
A bare minimum miner with a Cortex-A53 Allwinner H616 SoC made with KiCad


<p align="center">
     <img width="299" src="https://github.com/TechyGuy17/kryptokrona-mini-miner/blob/main/pics/main.png">
</p>

## Overview
A simple as possible SBC for mining kryptokrona (XKR), based on [Kononenko-K's h616 devboard](https://github.com/Kononenko-K/Allwinner_H616_Devboard/)

## [Hardware](Hardware)


The board features 64-bit 1.5GHz Quad-Core Cortex-A53 Allwinner H616 SOC, up to 8 Gbit (1 GB) of FBGA-96 16x DDR3 RAM, Micro SD slot, USB HS Host connector and integrated CP2102 USB-UART converter. 4 layers; 3,5/3,5 mil; 0,35/0,15 via, 80u prepreg.
There are [KiCad project](/Hardware), [Gerber files](/Hardware/gerber) and [PDF](/Hardware/output.pdf) avaliable.

## Software
** NOT TESTED SOFTWARE, IT COMPILES BUT MIGHT NOT ACTUALLY WORK ** 
Due to the switch to the more accessable AXP313a, the project is no longer fully compatible with the Orange Pi zero 2- But there is a workaround!

For this guide we will be using armbian, since its lightweight and has support for our processor.

The recommended OS to run this in is Ubuntu 22.04

start by downloading this repo to get the necessary files

```git clone https://github.com/TechyGuy17/kryptokrona-mini-miner```

After that we want to download the "Armbian Builder"

```git clone https://github.com/armbian/build && cd build```

Now we will do a dry run of the builder to let it download all the sources and also fix the file structure

```./compile.sh build BOARD=orangepizero2 BRANCH=current BUILD_DESKTOP=no BUILD_MINIMAL=yes KERNEL_CONFIGURE=no RELEASE=bookworm```

Now we are ready to start doing the patching. If you havent moved around the folders you can use theese commands to do the whole process

```mkdir userpatches/kernel/archive/sunxi-6.6```
```cp ../kryptokrona-mini-miner/Patches/updated-tp-axp313a.patch userpatches/kernel/archive/sunxi-6.6 ```
```cp ../kryptokrona-mini-miner/Patches/updated-tp-axp313a-uboot.patch userpatches/u-boot/u-boot-sunxi```

What this does is move in a few files that make it so we switch out everything regarding the AXP305 to 313a

Now we are ready to build for real!

```./compile.sh build BOARD=orangepizero2 BRANCH=current BUILD_DESKTOP=no BUILD_MINIMAL=yes KERNEL_CONFIGURE=no RELEASE=bookworm```

After this, you should have an image ready to be flashed to a SD card and then ready to be booted! Plug in an wifi/ethernet adapter in the board and a USB-c cable from your computer to the miner and then it should light up! The board will show up as a serial device and can be accessed through software like puTTY or minicom. settings are 115200,8,1 meaning 115200 baud rate, 8 bits and one stop bit.

# Bonus
If you want xmrig preinstalled to your keep on reading!

Run the following command to move the required script to the right folder 
```mv ../kryptokrona-mini-miner/Patches/customie-image.sh userpatches```

When this is in place, rerun the compile 

```./compile.sh build BOARD=orangepizero2 BRANCH=current BUILD_DESKTOP=no BUILD_MINIMAL=yes KERNEL_CONFIGURE=no RELEASE=bookworm```

This will go a lot faster since most the code is cached by now