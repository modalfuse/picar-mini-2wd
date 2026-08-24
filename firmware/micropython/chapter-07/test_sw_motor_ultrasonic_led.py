"""第 7 章：按键控轮 + 超声灯光（推荐演示）"""
from machine import Pin, time_pulse_us
from motor_driver import Car
import time

SPEED = 60
TRIG_PIN, ECHO_PIN = 7, 10
THRESHOLD_CM, NEAR_CM = 100, 10
MEASURE_INTERVAL_MS = 120

sw20 = Pin(20, Pin.IN, Pin.PULL_UP)
sw21 = Pin(21, Pin.IN, Pin.PULL_UP)
led_red = Pin(5, Pin.OUT, value=0)
led_green = Pin(6, Pin.OUT, value=0)
trig = Pin(TRIG_PIN, Pin.OUT, value=0)
echo = Pin(ECHO_PIN, Pin.IN)
car = Car()
car.stop()
STATE_NAME = ("停止", "前进", "反转")


def apply_motor_state(motor, state):
    if state == 1:
        motor.forward(SPEED)
    elif state == 2:
        motor.backward(SPEED)
    else:
        motor.stop()


def measure_cm():
    trig.value(0)
    time.sleep_us(5)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    try:
        dur = time_pulse_us(echo, 1, 30000)
    except OSError:
        return -1
    if dur < 0:
        return -1
    return dur * 0.0343 / 2


def blink_period_ms(d_cm):
    if d_cm <= NEAR_CM:
        return 50
    return int(50 + (d_cm - NEAR_CM) * (500 - 50) / (THRESHOLD_CM - NEAR_CM))


def update_distance_led(d_cm, last_toggle):
    if d_cm < 0:
        led_green.value(0)
        led_red.value(0)
        return last_toggle
    if d_cm >= THRESHOLD_CM:
        led_green.value(1)
        led_red.value(0)
        return last_toggle
    led_green.value(0)
    period = blink_period_ms(d_cm)
    now = time.ticks_ms()
    if time.ticks_diff(now, last_toggle) >= period // 2:
        led_red.value(not led_red.value())
        return now
    return last_toggle


print("按键控轮 + 超声灯, Ctrl-C 退出")
state_l = state_r = 0
last20, last21 = sw20.value(), sw21.value()
last_measure = last_toggle = time.ticks_ms()
try:
    while True:
        v20, v21 = sw20.value(), sw21.value()
        if v20 == 0 and last20 == 1:
            state_r = (state_r + 1) % 3
            apply_motor_state(car.right, state_r)
            print("右轮", STATE_NAME[state_r])
            time.sleep_ms(180)
        if v21 == 0 and last21 == 1:
            state_l = (state_l + 1) % 3
            apply_motor_state(car.left, state_l)
            print("左轮", STATE_NAME[state_l])
            time.sleep_ms(180)
        last20, last21 = v20, v21
        now = time.ticks_ms()
        if time.ticks_diff(now, last_measure) >= MEASURE_INTERVAL_MS:
            last_toggle = update_distance_led(measure_cm(), last_toggle)
            last_measure = now
        time.sleep_ms(10)
except KeyboardInterrupt:
    pass
finally:
    car.stop()
    car.deinit()
    led_red.value(0)
    led_green.value(0)
