"""
第 3 章：SW20 / SW21 按键测试（低有效）
SW21=左侧(GPIO21), SW20=右侧(GPIO20)
"""
from machine import Pin
import time

sw20 = Pin(20, Pin.IN, Pin.PULL_UP)
sw21 = Pin(21, Pin.IN, Pin.PULL_UP)

print("=== 按键测试 15 秒 ===")
print("SW21=左  SW20=右  按下=0")

last20, last21 = sw20.value(), sw21.value()
c20 = c21 = 0
t0 = time.ticks_ms()
while time.ticks_diff(time.ticks_ms(), t0) < 15000:
    v20, v21 = sw20.value(), sw21.value()
    if v20 == 0 and last20 == 1:
        c20 += 1
        print("SW20 按下 #{}".format(c20))
        time.sleep_ms(180)
    if v21 == 0 and last21 == 1:
        c21 += 1
        print("SW21 按下 #{}".format(c21))
        time.sleep_ms(180)
    last20, last21 = v20, v21
    time.sleep_ms(15)

print("完成: SW20={} SW21={}".format(c20, c21))
