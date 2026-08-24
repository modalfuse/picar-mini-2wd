"""状态灯：LED5 红/左，LED6 绿/右"""
from machine import Pin
import config


class StatusLed:
    def __init__(self):
        self.red = Pin(config.LED_RED, Pin.OUT, value=0)
        self.green = Pin(config.LED_GREEN, Pin.OUT, value=0)

    def off(self):
        self.red.value(0)
        self.green.value(0)

    def far(self):
        self.green.value(1)
        self.red.value(0)

    def near_toggle(self):
        self.green.value(0)
        self.red.value(not self.red.value())
