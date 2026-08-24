"""超声波测距模块 — Trig=GPIO7, Echo=GPIO10"""

from machine import Pin, time_pulse_us
import time

TRIG_PIN = 7
ECHO_PIN = 10


class Ultrasonic:
    def __init__(self, trig_pin=TRIG_PIN, echo_pin=ECHO_PIN):
        self.trig = Pin(trig_pin, Pin.OUT, value=0)
        self.echo = Pin(echo_pin, Pin.IN)

    def measure_cm(self):
        self.trig.value(0)
        time.sleep_us(5)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        try:
            dur = time_pulse_us(self.echo, 1, 30000)
        except OSError:
            return -1
        if dur < 0:
            return -1
        return dur * 0.0343 / 2
