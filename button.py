#!/usr/bin/env python3

import time

import RPi.GPIO as GPIO

from lights import sunset


def button_callback(channel):
    print("Button pushed")
    sunset(45)


def setup_listener():
    pin = 26
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback)
    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        setup_listener()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        lights.cleanup()
