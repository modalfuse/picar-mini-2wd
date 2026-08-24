"""
第 6 章：超声测距 + LED
>=1m 绿灯常亮; <1m 红灯频闪; 无效双灭
LED5(GPIO5)=红, LED6(GPIO6)=绿
"""
from machine import Pin
from ultrasonic import Ultrasonic
import time

THRESHOLD_CM = 100
NEAR_CM = 10
us = Ultrasonic()
led_red = Pin(5, Pin.OUT, value=0)
led_green = Pin(6, Pin.OUT, value=0)


def blink_period_ms(d_cm):
    if d_cm <= NEAR_CM:
        return 50
    return int(50 + (d_cm - NEAR_CM) * (500 - 50) / (THRESHOLD_CM - NEAR_CM))


print("超声+LED, Ctrl-C 退出")
last_toggle = time.ticks_ms()
n = 0
try:
    while True:
        d = us.measure_cm()
        n += 1
        if d < 0:
            led_green.value(0)
            led_red.value(0)
        elif d >= THRESHOLD_CM:
            led_green.value(1)
            led_red.value(0)
        else:
            led_green.value(0)
            period = blink_period_ms(d)
            now = time.ticks_ms()
            if time.ticks_diff(now, last_toggle) >= period // 2:
                led_red.value(not led_red.value())
                last_toggle = now
        if n % 5 == 0:
            print(d)
        time.sleep_ms(40)
except KeyboardInterrupt:
    pass
finally:
    led_red.value(0)
    led_green.value(0)
