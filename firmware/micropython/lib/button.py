"""板载轻触开关：低有效，边沿检测"""
from machine import Pin
import time
import config


class Button:
    def __init__(self, pin_num, debounce_ms=180):
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self.debounce_ms = debounce_ms
        self._last = self.pin.value()

    def pressed_edge(self):
        """按下边沿返回 True（松开->按下）"""
        v = self.pin.value()
        edge = (v == 0 and self._last == 1)
        self._last = v
        if edge:
            time.sleep_ms(self.debounce_ms)
            self._last = self.pin.value()
        return edge


sw_left = Button(config.SW_LEFT)
sw_right = Button(config.SW_RIGHT)
