"""第 7 章：按键控轮三态循环 + LED 指示轮状态"""
from machine import Pin
from motor_driver import Car
import time

SPEED = 60
sw20 = Pin(20, Pin.IN, Pin.PULL_UP)
sw21 = Pin(21, Pin.IN, Pin.PULL_UP)
led5 = Pin(5, Pin.OUT, value=0)
led6 = Pin(6, Pin.OUT, value=0)
car = Car()
car.stop()
STATE_NAME = ("停止", "前进", "反转")


def apply_state(motor, led, state):
    if state == 1:
        motor.forward(SPEED)
        led.value(1)
    elif state == 2:
        motor.backward(SPEED)
        led.value(1)
    else:
        motor.stop()
        led.value(0)


print("SW21->左轮  SW20->右轮  Ctrl-C 退出")
state_l = state_r = 0
last20, last21 = sw20.value(), sw21.value()
try:
    while True:
        v20, v21 = sw20.value(), sw21.value()
        if v20 == 0 and last20 == 1:
            state_r = (state_r + 1) % 3
            apply_state(car.right, led6, state_r)
            print("右轮", STATE_NAME[state_r])
            time.sleep_ms(180)
        if v21 == 0 and last21 == 1:
            state_l = (state_l + 1) % 3
            apply_state(car.left, led5, state_l)
            print("左轮", STATE_NAME[state_l])
            time.sleep_ms(180)
        last20, last21 = v20, v21
        time.sleep_ms(15)
except KeyboardInterrupt:
    pass
finally:
    car.stop()
    car.deinit()
    led5.value(0)
    led6.value(0)
