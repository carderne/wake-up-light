#!/usr/bin/env python3

import time
import threading

import RPi.GPIO as GPIO

from lights import sunset, cleanup

RUNNING = False
duration = 30


def reset():
    global RUNNING
    RUNNING = False


def pushed(channel):
    global RUNNING
    if not RUNNING:
        print("Button pushed")
        RUNNING = True
        sunset(duration)
        threading.Timer(10, reset).start()


def setup_listener():
    pin = 26
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=pushed)
    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        setup_listener()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        cleanup()
