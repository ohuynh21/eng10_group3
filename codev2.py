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

# Timer Section
MAX = 5
MAX_TIME = MAX * 60
timer = 0
#(MAX_TIME/10 * 0) * 60
# in minutes
interval = 0
count = 0

# Loop Section

while True:
    if (cp.button_a and timer == MAX_TIME):
        timer = 0
        interval = 0
        cp.pixels.fill((0,0,0))
    if (cp.button_a and timer < MAX_TIME):
        timer += MAX_TIME/10
        interval += 1
        cp.pixels[interval-1] = (0, 255, 0)
        sleep(0.5)
        print("WILL LOCK FOR", timer/60, "MINUTES")
        
    elif cp.button_b:
        print("LOCKED FOR", timer/60, "MINUTES")
        for i in range (0, interval):
            cp.pixels[i] = (255, 0, 0)
            sleep(0.25)
        servo.angle = 180
        
        while (timer != 0):
            sleep(1)
            count += 1
            if (count == MAX_TIME/10):
                cp.pixels[interval - 1] = (0, 0, 0)
                interval -= 1
                count = 0
            timer -= 1
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
