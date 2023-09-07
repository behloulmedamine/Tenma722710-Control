# Tenma722710-Control

Provides a basic controller (tested on Linux) for a **TENMA** DC power supply via serial interface. Working on python 2.7 and python 3.

- tenma\_72_2710.py (command line utility)
	
# What is this?

A small command line program / library to setup a **Tenma 72-2710** DC POWER SUPPLY from your computer via SERIAL.

# To install

It does not have many requirements, so you might just clone the repo and run it. install the following package first.

```
pip install pyserial
```

# Usage examples

Note that it can be connected via a usb to serial cable, or directly with the provided USB cable. In Linux it identifies the usb as Virtual Com Port , running dmesg to get where the /dev/ttyACMX device registerd and pointing tenmaControl.py to that device should work.

### Print the Tenma command help
```
./tenmaControl.py -h
```

### Get the Tenma model info
```
./tenmaControl.py -v /dev/ttyACM0
```

### Get the Tenma ON/OFF state
```
./tenmaControl.py -s /dev/ttyACM0
```

### Set the Tenma output to ON
```
./tenmaControl.py --on /dev/ttyACM0
```

### Set the Tenma output to OFF
```
./tenmaControl.py --oFF /dev/ttyACM0
```

### Set the Tenma Voltage (mV)
```
./tenmaControl.py -sv 5000 /dev/ttyACM0
```

### Get the Tenma Voltage (V)
```
./tenmaControl.py -gv /dev/ttyACM0
```

### Set the Tenma Current (mA)
```
./tenmaControl.py -sc 200 /dev/ttyACM0
```

### Get the Tenma Current (A)
```
./tenmaControl.py -gc /dev/ttyACM0
```

