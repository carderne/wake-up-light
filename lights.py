#!/usr/bin/env python3

import time
import sys

import pigpio

pi = pigpio.pi()

pins = {"red": 5, "green": 6, "blue": 13}
for pin in pins.values():
    pi.set_PWM_frequency(pin, 390)


def sunrise(duration):
    wait = 60 * duration / 765
    for x in range(766):
        pi.set_PWM_dutycycle(pins["red"], x / 3)
        if x > 255:
            pi.set_PWM_dutycycle(pins["green"], x / 2 - 127.5)
        if x > 510:
            pi.set_PWM_dutycycle(pins["blue"], x - 510)
        time.sleep(wait)
    time.sleep(15 * 60)


def sunset(duration):
    wait = 60 * duration / 765
    for x in range(765, -1, -1):
        pi.set_PWM_dutycycle(pins["red"], x / 3)
        pi.set_PWM_dutycycle(pins["green"], 0.3 * x / 3)
        time.sleep(wait)


def cleanup():
    for pin in pins.values():
        pi.set_PWM_dutycycle(pin, 0)
    pi.stop()


if __name__ == "__main__":
    func = sys.argv[1]
    duration = float(sys.argv[2])
    try:
        if func == "sunrise":
            sunrise(duration)
        else:
            sunset(duration)
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
