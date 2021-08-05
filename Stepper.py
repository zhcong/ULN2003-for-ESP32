import time

# only test for uln2003
class Stepper:
    # spec: http://www.geeetech.com/wiki/index.php/Stepper_Motor_5V_4-Phase_5-Wire_%26_ULN2003_Driver_Board_for_Arduino#Interfacing_circuits
    # from spec- Speed Variation Ratio ：1/64, the ratio between input wheel to output wheel is 64
    # from the spec (5.625'/64) angle for one HALF_STEP, and for one internal cycle you need 8 HALF_STEPs
    # so for 360' is: (360/(5.625'/64))/8=512(before any step) and multiply it by one cycle(8 HALF_STEPs or 4 FULL_STEPs)
    FULL_ROTATION = 512 # int(4075.7728395061727 / 8) # http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html

    HALF_STEP = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
    ]

    FULL_STEP = [
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    def __init__(self, mode, pin1, pin2, pin3, pin4, delay):
    	if mode=='FULL_STEP':
        	self.mode = self.FULL_STEP
        else:
        	self.mode = self.HALF_STEP
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.delay = delay  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP
        
        # Initialize all to 0
        self.reset()
        
    def step(self, count, direction=1):
        """Rotate count steps. direction = -1 means backwards"""
        for x in range(count):
            for bit in self.mode[::direction]:
                self.pin1(bit[0])
                self.pin2(bit[1])
                self.pin3(bit[2])
                self.pin4(bit[3])
                time.sleep_ms(self.delay)
        self.reset()
	
    # this is added angle not absolute- call it addAngle()
    # the direction can calculate if the angle is negative, no need this input
    def addAngle(self, angle):
	if angle < 0 : direction = -1
        if angle >= 0 : direction = 1
        self.step(int(self.FULL_ROTATION * abs(angle) / 360), direction)
	
    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        self.pin1(0) 
        self.pin2(0) 
        self.pin3(0) 
        self.pin4(0)

def create(pin1, pin2, pin3, pin4, delay=2, mode='HALF_STEP'):
	return Stepper(mode, pin1, pin2, pin3, pin4, delay)
