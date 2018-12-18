import Stepper
from machine import Pin
'''
IN1 -->  16
IN2 -->  17
IN3 -->  5
IN4 -->  18
'''
s1 = Stepper.create(Pin(16,Pin.OUT),Pin(17,Pin.OUT),Pin(5,Pin.OUT),Pin(18,Pin.OUT), delay=2)
s1.step(100)
s1.step(100,-1)
s1.angle(180)
s1.angle(360,-1)