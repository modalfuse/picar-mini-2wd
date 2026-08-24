"""
第 8 章综合主程序（可开机自启）
行为: 左右键三态控轮 + 超声远绿近红
上电先延时, 便于 Ctrl-C 打断
"""
import time
import config
from button import sw_left, sw_right
from status_led import StatusLed
from motor_driver import Car
from ultrasonic import Ultrasonic

STATE_NAME = ("停止", "前进", "反转")


def apply_motor(motor, state):
    if state == 1:
        motor.forward(config.SPEED)
    elif state == 2:
        motor.backward(config.SPEED)
    else:
        motor.stop()


def blink_period_ms(d_cm):
    if d_cm <= config.NEAR_CM:
        return 50
    return int(
        50
        + (d_cm - config.NEAR_CM)
        * (500 - 50)
        / (config.THRESHOLD_CM - config.NEAR_CM)
    )


print("[main] 启动倒计时 {}s, Ctrl-C 可中止...".format(config.BOOT_DELAY_S))
time.sleep(config.BOOT_DELAY_S)

car = Car()
car.stop()
leds = StatusLed()
us = Ultrasonic()
state_l = state_r = 0
last_measure = last_toggle = time.ticks_ms()

print("[main] 进入主循环: SW21 左轮 / SW20 右轮 + 超声灯")
try:
    while True:
        if sw_right.pressed_edge():
            state_r = (state_r + 1) % 3
            apply_motor(car.right, state_r)
            print("右轮", STATE_NAME[state_r])
        if sw_left.pressed_edge():
            state_l = (state_l + 1) % 3
            apply_motor(car.left, state_l)
            print("左轮", STATE_NAME[state_l])

        now = time.ticks_ms()
        if time.ticks_diff(now, last_measure) >= config.MEASURE_INTERVAL_MS:
            d = us.measure_cm()
            if d < 0:
                leds.off()
            elif d >= config.THRESHOLD_CM:
                leds.far()
            else:
                period = blink_period_ms(d)
                if time.ticks_diff(now, last_toggle) >= period // 2:
                    leds.near_toggle()
                    last_toggle = now
            last_measure = now
        time.sleep_ms(10)
except KeyboardInterrupt:
    print("[main] 用户中断")
finally:
    car.stop()
    car.deinit()
    leds.off()
    print("[main] 已停止")
