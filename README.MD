# ULN2003 for ESP32
uln2003 for `MicroPython` has been in github, here's the [link](https://github.com/IDWizard/uln2003). But it's work for `microbit`, so I change a little to transplant for my NodeMCU's `ESP-32s`. Here's the example:
```python
from stepper import Stepper
from machine import Pin

in1 = Pin(16,Pin.OUT)
in2 = Pin(17,Pin.OUT)
in3 = Pin(5,Pin.OUT)
in4 = Pin(18,Pin.OUT)
delay = 2
mode = 1 # 0 for half step, 1 for full step

def main() -> None:
    s1 = Stepper(in1, in2, in3, in4, delay, mode)
    s1.step(100)
    s1.step(100,-1)
    s1.angle(180)
    s1.angle(360,-1)
```
function `angle` is angle, and the PIN map:
`IN1` link `PIN_16`
`IN2` link `PIN_17`
`IN3` link `PIN_5`
`IN4` link `PIN_18`
My uln2003 board like this, and stepper runing:<br />
![uln2003](img/uln2003.jpg)      ![uln2003](img/stepper.gif)<br />
