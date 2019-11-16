#!/usr/bin/env python3

import RPi.GPIO as GPIO

import lights


def button_callback(channel):
    print("Button pushed")
    lights.sleep(45)


pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback)

try:
    message = input("Press enter to quit\n\n")
except KeyboardInterrupt:
    pass
finally:
    lights.cleanup()

GPIO.cleanup()
