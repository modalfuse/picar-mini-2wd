"""
2WD 电机驱动 (MicroPython) — 驱动板 v1.1 / TC1508A

左轮 motor1: GPIO1 / GPIO0
右轮 motor2: GPIO4 / GPIO3
方向: pin1=PWM、pin2=0 为正转(前进)
"""

from machine import Pin, PWM

LEFT_1 = 1
LEFT_2 = 0
RIGHT_1 = 4
RIGHT_2 = 3

PWM_FREQ = 1000
MAX_DUTY = 1023


class Motor:
    def __init__(self, pin1_num, pin2_num):
        self._pwm1 = PWM(Pin(pin1_num), freq=PWM_FREQ, duty=0)
        self._pwm2 = PWM(Pin(pin2_num), freq=PWM_FREQ, duty=0)

    def forward(self, speed=100):
        duty = int(MAX_DUTY * min(max(speed, 0), 100) / 100)
        self._pwm1.duty(duty)
        self._pwm2.duty(0)

    def backward(self, speed=100):
        duty = int(MAX_DUTY * min(max(speed, 0), 100) / 100)
        self._pwm1.duty(0)
        self._pwm2.duty(duty)

    def stop(self):
        self._pwm1.duty(0)
        self._pwm2.duty(0)

    def brake(self):
        self._pwm1.duty(MAX_DUTY)
        self._pwm2.duty(MAX_DUTY)

    def deinit(self):
        self._pwm1.deinit()
        self._pwm2.deinit()


class Car:
    def __init__(self):
        self.left = Motor(LEFT_1, LEFT_2)
        self.right = Motor(RIGHT_1, RIGHT_2)

    def forward(self, speed=100):
        self.left.forward(speed)
        self.right.forward(speed)

    def backward(self, speed=100):
        self.left.backward(speed)
        self.right.backward(speed)

    def turn_left(self, speed=80):
        self.left.backward(speed)
        self.right.forward(speed)

    def turn_right(self, speed=80):
        self.left.forward(speed)
        self.right.backward(speed)

    def stop(self):
        self.left.stop()
        self.right.stop()

    def brake(self):
        self.left.brake()
        self.right.brake()

    def deinit(self):
        self.left.deinit()
        self.right.deinit()
