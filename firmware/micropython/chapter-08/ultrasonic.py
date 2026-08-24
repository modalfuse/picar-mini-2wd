"""超声波（读 config）"""
from machine import Pin, time_pulse_us
import time
import config


class Ultrasonic:
    def __init__(self):
        self.trig = Pin(config.ULTRASONIC_TRIG, Pin.OUT, value=0)
        self.echo = Pin(config.ULTRASONIC_ECHO, Pin.IN)

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
