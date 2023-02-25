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

# User Specified Max Time (minutes)

MAX = 5

# Timer Variables
MAX_TIME = MAX * 60
timer = 0
interval = 0
count = 0

# Loop Section

while True:
    # OVERFLOW DETECTION
    if (cp.button_a and timer == MAX_TIME):
        timer = 0
        interval = 0
        cp.pixels.fill((0,0,0))
    # SET LOCK DURATION
    if (cp.button_a and timer < MAX_TIME):
        timer += MAX_TIME/10
        interval += 1
        cp.pixels[interval-1] = (0, 255, 0)
        sleep(0.5)
        print("WILL LOCK FOR", timer/60, "MINUTES")
    # SET LOCK    
    elif cp.button_b:
        print("LOCKED FOR", timer/60, "MINUTES")
        # LOCKING ANIMATION
        for i in range (0, interval):
            cp.pixels[i] = (255, 0, 0)
            sleep(0.25)
        servo.angle = 180
        
        # TIMER
        while (timer != 0):
            sleep(1)
            count += 1
            # TIME REMAINING ANIMATION
            if (count == MAX_TIME/10):
                cp.pixels[interval - 1] = (0, 0, 0)
                interval -= 1
                count = 0
            timer -= 1
            # PRINT REMANING TIME FOR DEBUGGING
            print(timer, "SECONDS REMAINING")

        # UNLOCK
        servo.angle = 0
        timer = 0
        cp.pixels.fill((0,255,0))
        sleep(0.25)
        cp.pixels.fill((0,0,0))
        print("UNLOCKED")
    else:
        continue
