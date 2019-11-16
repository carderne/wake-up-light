#!/usr/bin/env python3

import time
import sys

import pigpio

pi = pigpio.pi()

pins = {"red": 5, "green": 6, "blue": 13}
for pin in pins.values():
    pi.set_PWM_frequency(pin, 200)


def wake(duration):
    wait = 60 * duration / 100
    for x in range(101):
        pi.set_PWM_dutycycle(pins["red"], 2.55 * (x))
        if x > 33:
            pi.set_PWM_dutycycle(pins["green"], 2.55 * (1.5 * x - 50))
        if x > 66:
            pi.set_PWM_dutycycle(pins["blue"], 2.55 * (3 * x - 200))
        time.sleep(wait)
    time.sleep(15 * 60)


def sleep(duration):
    wait = 60 * duration / 100
    for x in range(101):
        pi.set_PWM_dutycycle(pins["red"], 2.55 * (100 - x))
        pi.set_PWM_dutycycle(pins["green"], 2.55 * (50 - 0.5 * x))
        time.sleep(wait)


def cleanup():
    for pin in pins.values():
        pi.set_PWM_dutycycle(pin, 0)
    pi.stop()


if __name__ == "__main__":
    func = sys.argv[1]
    duration = float(sys.argv[2])
    try:
        if func == "wake":
            wake(duration)
        else:
            sleep(duration)
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
