"""第 5 章：整车 8 项电机测试"""
from motor_driver import Car
import time

SPEED = 60
car = Car()
tests = [
    ("左轮正转", lambda: car.left.forward(SPEED)),
    ("左轮反转", lambda: car.left.backward(SPEED)),
    ("右轮正转", lambda: car.right.forward(SPEED)),
    ("右轮反转", lambda: car.right.backward(SPEED)),
    ("前进", lambda: car.forward(SPEED)),
    ("后退", lambda: car.backward(SPEED)),
    ("左转", lambda: car.turn_left(SPEED)),
    ("右转", lambda: car.turn_right(SPEED)),
]
print("=== 电机测试开始 ===")
try:
    for i, (name, action) in enumerate(tests):
        print("{}/{} {}".format(i + 1, len(tests), name))
        action()
        time.sleep(1)
        car.stop()
        time.sleep_ms(300)
finally:
    car.stop()
    car.deinit()
print("=== 测试完成 ===")
