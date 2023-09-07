#!/usr/bin/env python3


"""
    Command line tenma control program for Tenma72_2710 bank power supply
"""

import argparse

"""
# TODO this is just a trick so tenmaControl runs cleanly from both the source tree
# and the pip installation


try:
    from tenma.tenmaDcLib import instantiate_tenma_class_from_device_response, TenmaException
except Exception:
    from tenmaDcLib import instantiate_tenma_class_from_device_response, TenmaException
"""

from tenmaDcLib import instantiate_tenma_class_from_device_response, TenmaException

def main():
    parser = argparse.ArgumentParser(description='Control a Tenma 72-2710 power supply connected to a serial port')
    parser.add_argument('device', default="/dev/ttyACM0")
    parser.add_argument('-sv', '--setvoltage', help='set voltage in mV', required=False, type=int)
    parser.add_argument('-sc', '--setcurrent', help='set current in mA', required=False, type=int)
    parser.add_argument('-gc', '--getcurrent', help='returns the output current settings', action="store_true", default=False)
    parser.add_argument('-gv', '--getvoltage', help='returns the output voltage settings', action="store_true", default=False)
    parser.add_argument('--on', help='Set output to ON', action="store_true", default=False)
    parser.add_argument('--off', help='Set output to OFF', action="store_true", default=False)                 
    parser.add_argument('-s', '--state', help='output state', action="store_true", default=False)       
    parser.add_argument('-v', '--version', help='Retrieve and print system status', required=False, action="store_true", default=False)
    parser.add_argument('--verbose', help='Chatty program', action="store_true", default=False)
    parser.add_argument('--debug', help='print serial commands', action="store_true", default=False)
    parser.add_argument('-c', '--channel', help='channel to set (if not provided, 1 will be used)', required=False, type=int, default=1)
    args = vars(parser.parse_args())
    
    T = None
    try:
        VERB = args["verbose"]
        T = instantiate_tenma_class_from_device_response(args["device"], args["debug"])
        
        if args["version"]:
            print("VERSION ==> ", T.getVersion())

        if args["off"]:
            if VERB:
                print("Turning OUTPUT OFF")
            T.OFF()

        if args["on"]:
            if VERB:
                print("Turning OUTPUT ON")
            T.ON()

        if args["state"]:
            if VERB:
                print("Retrieving status")
            print(T.getStatus()["outEnabled"])

        if args["setvoltage"]:
            if VERB:
                print("Setting voltage to ", args["setvoltage"])
            T.setVoltage(args["channel"], args["setvoltage"])

        if args["setcurrent"]:
            if VERB:
                print("Setting current to ", args["setcurrent"])
            T.setCurrent(args["channel"], args["setcurrent"])

        if args["getcurrent"]:
            if VERB:
                print("Retrieving Current value")
            print(T.readCurrent(args["channel"]))

        if args["getvoltage"]:
            if VERB:
                print("Retrieving Voltage value")
            print(T.readVoltage(args["channel"]))

    except TenmaException as e:
        print("Lib ERROR: ", repr(e))
    finally:
        if VERB:
            print("Closing connection")
        if T:
            T.close()


if __name__ == "__main__":
    main()
