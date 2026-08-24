"""
第 3 章：按键翻转 LED（与实物左右一致）
左侧: SW21 -> LED5 红色(GPIO5)
右侧: SW20 -> LED6 绿色(GPIO6)
"""
from machine import Pin
import time

sw20 = Pin(20, Pin.IN, Pin.PULL_UP)   # 右键
sw21 = Pin(21, Pin.IN, Pin.PULL_UP)   # 左键
led_red = Pin(5, Pin.OUT, value=0)    # LED5 红/左
led_green = Pin(6, Pin.OUT, value=0)  # LED6 绿/右

print("左键SW21=红灯LED5  右键SW20=绿灯LED6  Ctrl-C退出")
last20, last21 = sw20.value(), sw21.value()
try:
    while True:
        v20, v21 = sw20.value(), sw21.value()
        if v21 == 0 and last21 == 1:
            led_red.value(not led_red.value())
            print("左侧红灯 LED5", "ON" if led_red.value() else "OFF")
            time.sleep_ms(180)
        if v20 == 0 and last20 == 1:
            led_green.value(not led_green.value())
            print("右侧绿灯 LED6", "ON" if led_green.value() else "OFF")
            time.sleep_ms(180)
        last20, last21 = v20, v21
        time.sleep_ms(15)
except KeyboardInterrupt:
    pass
finally:
    led_red.value(0)
    led_green.value(0)
