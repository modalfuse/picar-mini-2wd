"""
第 2 章：板载 LED 闪烁
LED5(GPIO5)=红/左, LED6(GPIO6)=绿/右, 高电平点亮
"""
from machine import Pin
import time

led_red = Pin(5, Pin.OUT, value=0)
led_green = Pin(6, Pin.OUT, value=0)

print("点亮绿灯 1s")
led_green.value(1)
time.sleep(1)
led_green.value(0)

print("点亮红灯 1s")
led_red.value(1)
time.sleep(1)
led_red.value(0)

print("红绿交替闪烁 6 次")
for _ in range(6):
    led_green.value(1)
    led_red.value(0)
    time.sleep_ms(250)
    led_green.value(0)
    led_red.value(1)
    time.sleep_ms(250)

led_red.value(0)
led_green.value(0)
print("完成")
