#!/usr/bin/env python
#
# Usage: relay.py relay-number|name reset|power|power-down [number-of-seconds]
#
# Example 1 (force power down): relay.py 1 power-down 5
# Example 2 (power up/down): relay.py 1 power 0.02
# Example 3 (cold reset): relay.py 1 reset 0.02
#
# number-of-seconds is optional and the examples use the default values
#

from __future__ import print_function

import sys
import time

from relay_lib_seeed import *

# TODO

def process_loop():
    # turn all of the relays on
    relay_all_on()
    # wait a second
    time.sleep(1)
    # turn all of the relays off
    relay_all_off()
    # wait a second
    time.sleep(1)

    # now cycle each relay every second in an infinite loop
    while True:
        for i in range(1, 5):
            relay_on(i)
            time.sleep(1)
            relay_off(i)

def usage(cmd):
    print("Usage:", cmd, " [-h] relay-number [reset|power|power-down] [relay-on-time-seconds]")
    print("relay-number:    1,2,3,4")


# TODO: support use of names instead of relay number
RELAY = 1
ACTION = "reset"
SECONDS = None

if __name__ == "__main__":

    if len(sys.argv) == 1 or sys.argv[1] == "-h" :
            usage(sys.argv[0])
            quit()

    if len(sys.argv) > 1:
        RELAY=int(sys.argv[1])
    if len(sys.argv) > 2:
        ACTION=sys.argv[2]
    if len(sys.argv) > 3:
        SECONDS=float(sys.argv[3])

# default relay time
if SECONDS is None:
    if ACTION == "reset" :
        SECONDS = 0.01
    elif ACTION == "power" :
        SECONDS = 0.02
    elif ACTION == "power-down" :
        SECONDS = 5
    else :
        usage(sys.argv[0])
        quit()

print("Relay", RELAY, ACTION, SECONDS)

# activate relay
relay_on(RELAY)
time.sleep(SECONDS)
relay_off(RELAY)
