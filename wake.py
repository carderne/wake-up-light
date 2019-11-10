#!/usr/bin/env python3

import time
import sys

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

red_pin = 22
green_pin = 23
blue_pin = 24

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

freq = 100
red = GPIO.PWM(red_pin, freq)
green = GPIO.PWM(green_pin, freq)
blue = GPIO.PWM(blue_pin, freq)

red.start(100)
green.start(100)
blue.start(100)

duration = int(sys.argv[1])
sleep = 60 * duration / 100
try:
    pass
    for x in range(101):
        time.sleep(sleep)
        red.ChangeDutyCycle(100-x)
        if x > 33:
            green.ChangeDutyCycle(100-1.5*x+50)
        if x > 66:
            blue.ChangeDutyCycle(100-3*x+200)

    time.sleep(15 * 60)

except Exception as e: 
    print(e)

finally:
    GPIO.cleanup()
