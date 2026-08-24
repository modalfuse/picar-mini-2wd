"""第 6 章：超声波串口测距"""
from ultrasonic import Ultrasonic
import time

us = Ultrasonic()
print("Trig=7 Echo=10, 共 50 次")
for i in range(50):
    d = us.measure_cm()
    if d < 0:
        print("[{:>2d}] 超量程/无回波".format(i + 1))
    else:
        print("[{:>2d}] {:6.1f} cm".format(i + 1, d))
    time.sleep_ms(200)
print("完成")
