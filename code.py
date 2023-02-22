import board
import pwmio
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep
import random

# Setup Section
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section

# Loop Section
timer = 0
while True:
    if (cp.button_a and timer < 10):
        timer += 1
        sleep(0.5)
        print(timer)
    elif cp.button_b:
        print("locked")
        servo.angle = 180
        
        sleep(timer)
        servo.angle = 0
        timer = 0
    else:
        continue
