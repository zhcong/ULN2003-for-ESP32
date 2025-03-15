from stepper import Stepper

in1 = 16
in2 = 17
in3 = 5
in4 = 18
delay = 2
mode = 1 # 0 for half step, 1 for full step

def main() -> None:
    s1 = Stepper(in1, in2, in3, in4, delay, mode)
    s1.step(100)
    s1.step(100,-1)
    s1.angle(180)
    s1.angle(360,-1)