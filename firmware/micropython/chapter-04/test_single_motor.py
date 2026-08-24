"""第 4 章：单电机正反转与调速"""
from motor_driver import Car
import time

car = Car()
SPEEDS = (40, 70, 100)

try:
    for name, motor in (("左轮", car.left), ("右轮", car.right)):
        for sp in SPEEDS:
            print(name, "正转", sp)
            motor.forward(sp)
            time.sleep(1)
            motor.stop()
            time.sleep_ms(300)
            print(name, "反转", sp)
            motor.backward(sp)
            time.sleep(1)
            motor.stop()
            time.sleep_ms(300)
finally:
    car.stop()
    car.deinit()
print("完成")
