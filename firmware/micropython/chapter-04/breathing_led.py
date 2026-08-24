"""第 4 章：PWM 呼吸灯（左侧红灯 LED5）"""
from machine import Pin, PWM
import time

pwm = PWM(Pin(5), freq=1000, duty=0)  # LED5 红/左
try:
    while True:
        for d in range(0, 1024, 16):
            pwm.duty(d)
            time.sleep_ms(12)
        for d in range(1023, -1, -16):
            pwm.duty(d)
            time.sleep_ms(12)
except KeyboardInterrupt:
    pass
finally:
    pwm.duty(0)
    pwm.deinit()
