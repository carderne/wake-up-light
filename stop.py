#!/usr/bin/env python3

import json

import pigpio

pi = pigpio.pi()
for pin in range(30):
    try:
        pi.set_mode(pin, pigpio.OUTPUT)
        pi.write(pin, 0)
    except Exception as e:
        pass
pi.stop()
