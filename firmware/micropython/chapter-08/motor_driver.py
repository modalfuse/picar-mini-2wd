"""电机驱动（读 config）"""
from machine import Pin, PWM
import config


class Motor:
    def __init__(self, pin1_num, pin2_num):
        self._pwm1 = PWM(Pin(pin1_num), freq=config.PWM_FREQ, duty=0)
        self._pwm2 = PWM(Pin(pin2_num), freq=config.PWM_FREQ, duty=0)

    def forward(self, speed=100):
        duty = int(config.MAX_DUTY * min(max(speed, 0), 100) / 100)
        self._pwm1.duty(duty)
        self._pwm2.duty(0)

    def backward(self, speed=100):
        duty = int(config.MAX_DUTY * min(max(speed, 0), 100) / 100)
        self._pwm1.duty(0)
        self._pwm2.duty(duty)

    def stop(self):
        self._pwm1.duty(0)
        self._pwm2.duty(0)

    def deinit(self):
        self._pwm1.deinit()
        self._pwm2.deinit()


class Car:
    def __init__(self):
        self.left = Motor(config.LEFT_MOTOR_1, config.LEFT_MOTOR_2)
        self.right = Motor(config.RIGHT_MOTOR_1, config.RIGHT_MOTOR_2)

    def stop(self):
        self.left.stop()
        self.right.stop()

    def deinit(self):
        self.left.deinit()
        self.right.deinit()
